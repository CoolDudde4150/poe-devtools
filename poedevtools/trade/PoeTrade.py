import json
import requests
import poedevtools.trade.request_pb2 as PoeRequest
from google.protobuf.json_format import MessageToJson, MessageToDict
import math
import pprint
from google.protobuf import text_format

# TODO: Find a way to print all the fields of a protobuf including empty ones.
# TODO: Add setters and getters for parts of the protobuf
class PoeTrade:
    search_URL = "https://www.pathofexile.com/api/trade/search/"
    fetch_URL = "https://www.pathofexile.com/api/trade/fetch/"

    search_params = PoeRequest.PoeTradeRequest()

    response = {}
    
    def __init__(self):
        # There always needs to be a value for the league
        self.league = "Standard"

    def print_query(self):
    	print(text_format.MessageToString(self.search_params, as_utf8 = True))

    def get_query(self):
        return self.search_params

    def set_query(self, query):
        self.search_params = query
    
    def get_saved_response(self):
        return self.response

    # TODO: It would likely be a good idea to return the error received and let the application maker
    #       deal with it.
    # TODO: Add functionality to use a dict or plain json.
    # TODO: Add custom start and stop functionality
    # Performs the actual search with a query on the poe trade api.
    #
    # PoeTradeRequest - A protobuf object provided with this object.
    # num_get - The number of results you want returned.
    # save_response - This object can save a search response if wanted for later reference
    # start - A custom search start position. Defaults to 0 if not set
    def search(self, PoeTradeRequest = None, num_get = 10, save_response = False, start = None):
        # Use the saved trade request if none are provided
        if PoeTradeRequest != None:
            request = PoeTradeRequest
        else:
            request = self.search_params

        # Get the id responses from path of exile trade
        response = requests.post(url = self.search_URL + self.league, json = MessageToDict(request))

        dict_response = response.json()

        print(dict_response)
        # If the query return nothing, return nothing
        if "result" not in dict_response:
            return None

        # If there are less results than the requested amount, get all of them.
        if len(dict_response) < num_get:
            num_get = len(dict_response)

        # we can only search for 10 id's per query, so store every iteration of 10 in items.
        items = {"result": []}

        start = 0
        while (num_get > 0):
            # It works but I know there is a cleaner way with modulus >:^()
            if num_get > 10:
                end = start + 10
            else:
                end = start + num_get
            num_get -= 10

            fetch_URL_temp = self.fetch_URL
            for result in dict_response["result"][start:end]:
                fetch_URL_temp += result + ","
            fetch_URL_temp = fetch_URL_temp[:-1] + "?query=" + dict_response["id"]

            items_response = requests.get(fetch_URL_temp)
            for id in items_response.json()["result"]:
                items["result"].append(id)

            start = end

        if(save_response):
            self.response = items

        return items

trade = PoeTrade()
trade.print_query()