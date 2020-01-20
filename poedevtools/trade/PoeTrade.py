import json
import requests
import poedevtools.trade.request_pb2 as PoeRequest
from google.protobuf.json_format import MessageToJson, MessageToDict

class PoeTrade:
    URL = "https://www.pathofexile.com/api/trade/search/"

    searchParams = PoeRequest.PoeTradeRequest()
    
    def __init__(self):
        # There always needs to be a value for the league
        self.league = "Standard"

    def print_query(self):
    	print(self.searchParams)