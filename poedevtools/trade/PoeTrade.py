import json
import requests
import poedevtools.trade.request_pb2 as PoeRequest
from google.protobuf.json_format import MessageToJson, MessageToDict

class PoeTrade:
    search_URL = "https://www.pathofexile.com/api/trade/search/"
    fetch_URL = "https://www.pathofexile.com/api/trade/fetch/"

    search_params = PoeRequest.PoeTradeRequest()
    
    def __init__(self):
        # There always needs to be a value for the league
        self.league = "Standard"

    def print_query(self):
    	print(self.search_params)

    def get_query(self):
        return self.search_params

    def set_query(self, query):
        self.search_params = query
    
    def search(self, PoeTradeRequest = None):
        if PoeTradeRequest != None:
            request = PoeTradeRequest
        response = requests.post(url = self.search_URL + self.league, json = MessageToDict(request))

        dict_response = response.json()
        fetch_URL_temp = self.fetch_URL

        for result in dict_response["result"][0:10]:
            fetch_URL_temp += result + ","
        fetch_URL_temp = fetch_URL_temp[:-1] + "?query=" + dict_response["id"]

        items_response = requests.get(fetch_URL_temp)

        return items_response.json()

        

# cool = PoeTrade()

# request = PoeRequest.PoeTradeRequest()

# request.query.status.option = "online"
# print(request)

# cool.set_query(request)

# print(cool.search())