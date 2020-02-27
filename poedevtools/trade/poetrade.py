"""Functionality to interact with trade api endpoint of Path of Exile.

This includes:
* Getting current running leagues
* Getting current static list of current in game items
* Getting current possible list of stats that can be on in game items
* Getting static data, including relative paths to image files.
* Searching and fetching search on the official trade api
* Seeing a list of currently ignored accounts and ignoring/unignoring accounts.

This class should encapsulate all the information that the official trade site has availible to it. 
I'm currently unsure of how live search works, so this class may not have the functionality for that.

Raises:
    ValueError: If the input query is not a valid type
"""

import json
import requests

from google.protobuf.json_format import MessageToDict
from google.protobuf import text_format
import poedevtools.trade.trade_request_pb2 as PoeRequest

# TODO: Find a way to print all the fields of a protobuf including empty ones.
# TODO: Add setters and getters for parts of the protobuf
class PoeTrade:
    """Base class for manipulating the PoE official trade API

    Args:
        league (str): The league of Path of Exile to search the API. Optional, defaults to standard.
        query (dict|PoeTradeRequest proto|str): A custom json-like message. Optional, defaults to an empty PoeTradeRequest
        response (dict): A save of a search result. Optional, defaults to None
    """
    
    trade_api_startpoint = "https://www.pathofexile.com/api/trade/"

    def __init__(
        self,
        league="standard",
        query=PoeRequest.PoeTradeRequest(),
        response=None,
        poesessid = ""
    ):
        self.league = league
        self.query = query
        self.response = response
        # Unsure if I want immediate access to poesessid :/
        self.__poesessid = poesessid

    def print_query(self):
        """Prints the query using the protobuf standard. Dont use if not protobuf
        """

        print(text_format.MessageToString(self.query, as_utf8=True))

    def reset_query(self):
        """Resets the saved query to an empty query.
        """

        self.query = PoeRequest.PoeTradeRequest()

    def search(
        self, query=None, num_get=10, start=0, save_response=False, save_query=False
    ):
        """Performs a search with a query against the PoE Trade API.

        Uses a form of json query against the trade API. Natively, the requests package uses dict objects. 
        It is therefore slightly more efficient to use a dict object for the input. Due to the nature of
        the PoE API limiting the number of requests per second, the effect is extremely negligible.

        This function can support a dict object, PoeTradeRequest proto object or a json string.
        
        Args:
            query (dict|PoeTradeRequest proto|str): The query to be used against the api. Optional, defaults to using a saved query.
            num_get (int): The number of items to be returned. Optional, defaults to 10 (the maximum that can be done in one request)
            start (int):  A custom start position. Skips the first *start* responses. Optional, defaults to 0.
            save_response (bool): Whether the response should be saved within this object (it is still returned). Optional, defaults to false
            save_query (bool): Whether the input query should be saved within this object. Will set the saved query to None if nothing is provided.

        Returns:
            dict: The items that were returned from the search.
        """

        if save_query:
            self.save_query(query)

        # Use the saved trade request if none are provided
        if query is None:
            query = self.query

        # Convert it to a dict to send. The trade api seems to be very picky :(.
        dict_query = PoeTrade._convert2dict(query)

        # Get the id responses from path of exile trade. They are the ID of the items I guess.
        response = requests.post(
            url=self.trade_api_startpoint + "search/" + self.league, json=dict_query,
        ).json()

        # If the query returns nothing, return the error message response. It will still be a json/dict
        # Assume user application will deal with errors.
        if "result" not in response:
            return response

        # If there are less results than the requested amount, get all of them.
        if len(response["result"]) < num_get:
            num_get = len(response["result"])

        # We can only search for 10 id's per query, so store every iteration of 10 in items.
        items = {"result": []}

        while num_get > 0:
            # It works but Im pretty sure there is a cleaner way with modulus >:^()
            if num_get > 10:
                end = start + 10
            else:
                end = start + num_get
            num_get -= 10

            fetch_url = PoeTrade._get_fetch_url(response["result"][start:end], response["id"])

            items_response = requests.get(fetch_url)

            # Try to convert the response to json
            try:
                json_item_reponse = items_response.json()
            except json.JSONDecodeError as error:
                print(error.msg)
                # Not sure how I want to do this. Return a formatted dict with empty results? Need to see what other errors can occur
                return items

            for id_ in json_item_reponse["result"]:
                items["result"].append(id_)

            start = end

        if save_response:
            self.response = items

        return items

    def get_leagues(self):
        """Gets the current running leagues in Path of Exile

        Returns:
            dict: A dict of the leagues being run.
        """

        return requests.get(self.trade_api_startpoint + "data/leagues/").json()

    def get_items(self):
        """Gets the all the currently possible items in Path of Exile
        
        Returns:
            dict: A dict of all the items
        """

        return requests.get(self.trade_api_startpoint + "data/items/").json()

    def get_stats(self):
        """Gets all of the stats that can currently occur on the item in Path of Exile
        
        Returns:
            dict: A dict of all the possible stats
        """

        return requests.get(self.trade_api_startpoint + "data/stats/").json()

    def get_static(self):
        """Gets all of the static data information from Path of Exile, including relative paths to image files
        
        Returns:
            dict: A dict of all the static data
        """

        return requests.get(self.trade_api_startpoint + "data/static/").json()

    def get_ignored_accounts(self, poesessid=None):
        """Gets all of the ignored accounts on the trade api based on a poesessid.
        
        Args:
            poesessid (str, optional): The poesessid cookie value that can be obtained from PathofExile.com. Defaults to self.__poesessid.
        
        Returns:
            dict: A dict of ignored accounts.
        """
        if poesessid is None:
            poesessid = self.__poesessid

        cookies = self._populate_trade_cookie(poesessid)
        
        return requests.get(self.trade_api_startpoint + "ignore/", cookies=cookies)

    def ignore_account(self, account_name, poesessid=None):
        """Ignores an account on the trade api based on their account name and your poesessid
        
        Args:
            account_name (str): The person who you want to ignore's account name
            poesessid (str, optional): The poesessid cookie value that can be obtained from PathofExile.com. Defaults to self.__poesessid.
        
        Returns:
            requests.models.Response: A response to the request to ignore
        """
        cookies = self._populate_trade_cookie(poesessid)

        return requests.put(self.trade_api_startpoint + "ignore/" + account_name, cookies=cookies)

    def unignore_account(self, account_name, poesessid=None):
        cookies = self._populate_trade_cookie(poesessid)

        return requests.delete(self.trade_api_startpoint + "ignore/" + account_name, cookies=cookies)

    def set_poesessid(self, poesessid):
        """Sets the stored poesessid.
        
        Args:
            poesessid (str): [description]
        """
        self.__poesessid = poesessid


    def save_query(self, query):
        """Saves a query that has been made in this data structure.

        This query can be run through the search function by providing no query in the function call.

        Args:
            query (dict|PoeTradeRequest|str): The query to be saved.
        """

        self.query = query

    def _populate_trade_cookie(self, poesessid):
        """Populates a cookie dict with the poesessid to be sent to the api
        
        Args:
            poesessid (str): The poesessid cookie value that can be obtained from PathofExile.com.
        
        Returns:
            dict: A cookie to be sent with the requests package
        """
        if poesessid is None:
            poesessid = self.__poesessid
        
        return {"POESESSID": poesessid}

    @classmethod
    def _convert2dict(cls, query):
        """Converts any of the query types to the needed dict for sending on the request
        
        Args:
            query (dict|PoeTradeRequest|str): The query to be converted
        
        Returns:
            dict: The resultant 'jsonified' query
        """

        if isinstance(query, PoeRequest.PoeTradeRequest):
            return MessageToDict(query, preserving_proto_field_name=True)
        if isinstance(query, dict):
            return query
        if isinstance(query, str):
            return json.loads(query)        
        raise ValueError("query should be a dict, PoeTradeRequest or string")
    
    @classmethod
    def _get_fetch_url(cls, results, iden):
        """Populates a fetch url request with id's. 

        Probably a good change to turn this into a producer(?). Whatever the thing is that just returns the next thing in a list on call.
        
        Args:
            results (iterable of str): The list of id's produced from an api search.  
            iden (str): The identification number produced from the search.
        """
        # We query the trade api with the item ID's we retreived before here
        fetch_url_temp = cls.trade_api_startpoint + "fetch/"
        for result in results:
            fetch_url_temp += result + ","
        # The general url for this is just the fetch url with the query ID's added to the end separated by commas.
        fetch_url_temp = fetch_url_temp[:-1] + "?query=" + iden

        return fetch_url_temp
