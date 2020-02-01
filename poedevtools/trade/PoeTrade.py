import requests

from google.protobuf.json_format import MessageToJson, MessageToDict
from google.protobuf import text_format
import poedevtools.trade.trade_request_pb2 as PoeRequest
import json

# TODO: Find a way to print all the fields of a protobuf including empty ones.
# TODO: Add setters and getters for parts of the protobuf
class PoeTrade:
    """
    Master class for manipulating the PoE official trade API

    Args:
        league (str): The league of Path of Exile to search the API. Optional, defaults to "standard".
        search_params (dict|PoeTradeRequest proto|str): A custom json-like message. Optional, defaults to an empty PoeTradeRequest
        search_URL (str): URL to the search part of the trade API. Optional, defaults to https://www.pathofexile.com/api/trade/search/.
        fetch_URL (str): URL to the fetch part of the trade API.  Optional, defaults to https://www.pathofexile.com/api/trade/fetch/.
        response (dict): A save of a search result. Optional, defaults to an empty dict
    """
    
    def __init__(self,
                 league = "standard",
                 search_params = PoeRequest.PoeTradeRequest(),
                 search_URL = "https://www.pathofexile.com/api/trade/search/",
                 fetch_URL = "https://www.pathofexile.com/api/trade/fetch/",
                 response = {}):
        self.league = "Standard"
        self.search_params = search_params
        self.search_URL = search_URL
        self.fetch_URL = fetch_URL
        self.response = response

    def print_query(self):
        print(text_format.MessageToString(self.search_params, as_utf8=True))

    def get_query(self):
        return self.search_params

    def set_query(self, query):
        self.search_params = query

    def get_saved_response(self):
        return self.response

    def reset_query(self):

        self.search_params = PoeRequest.PoeTradeRequest()

    # TODO: It would likely be a good idea to return the error received and let the application maker
    #       deal with it.
    # TODO: Add functionality to use a dict or plain json.
    # TODO: Add custom start and stop functionality
    def search(self, poe_trade_request=None, num_get=10, save_response=False, start=0):
        """Performs a search with a query against the PoE Trade API.

        Uses a form of json query against the trade API. Natively, the requests package uses dict objects. 
        It is therefore slightly more efficient to use a dict object for the input. Due to the nature of
        the PoE API limiting the number of requests per second, the effect is extremely negligible.

        This function can support a dict object, PoeTradeRequest proto object or a json string.
        
        Args:
            poe_trade_request (dict|PoeTradeRequest proto|str): The query to be used against the api. Optional, 
            defaults to using a saved query.
            num_get (int): The number of items to be returned. Optional, defaults to 10 (the maximum that can be done in one request)
            save_response (bool): Whether the response should be saved within this object (it is still returned). Optional, defaults to false
            start (int):  A custom start position. Skips the first *start* responses. Optional, defaults to 0.

        Returns:
            dict: The items that were returned from the search.
        """
        # Use the saved trade request if none are provided
        if poe_trade_request is not None:
            request = poe_trade_request
        else:
            request = self.search_params

        # Convert it to a dict to send
        if isinstance(request, PoeRequest.PoeTradeRequest):
            json_query = MessageToDict(request, preserving_proto_field_name=True)
        elif isinstance(request, dict):
            json_query = request
        elif isinstance(request, str):
            json_query = json.loads(request)
        else:
            print("Not a valid type for PoeTradeRequest")
            return None

        # Get the id responses from path of exile trade
        response = requests.post(
            url=self.search_URL + self.league,
            json=json_query,
        )

        dict_response = response.json()

        # If the query return nothing, return the error message response. It will still be a json/dict
        if "result" not in dict_response:
            return dict_response

        # If there are less results than the requested amount, get all of them.
        if len(dict_response) < num_get:
            num_get = len(dict_response)

        # we can only search for 10 id's per query, so store every iteration of 10 in items.
        items = {"result": []}

        while num_get > 0:
            # It works but I know there is a cleaner way with modulus >:^()
            if num_get > 10:
                end = start + 10
            else:
                end = start + num_get
            num_get -= 10

            fetch_url_temp = self.fetch_URL
            for result in dict_response["result"][start:end]:
                fetch_url_temp += result + ","
            fetch_url_temp = fetch_url_temp[:-1] + "?query=" + dict_response["id"]

            items_response = requests.get(fetch_url_temp)

            # Try to convert the response to json
            try:
                json_item_reponse = items_response.json()
            except:
                # Not sure how I want to do this. Return a formatted dict with empty results? Need to see what other errors can occur
                return items

            for id_ in json_item_reponse["result"]:
                items["result"].append(id_)

            start = end

        if save_response:
            self.response = items

        return items
