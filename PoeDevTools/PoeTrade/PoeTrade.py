import json
import requests
import PoeDevTools.PoeTrade.request_pb2 as PoeRequest
from google.protobuf.json_format import MessageToJson, MessageToDict

class PoeTrade:
    URL = "https://www.pathofexile.com/api/trade/search/"

    searchParams = PoeRequest.PoeTradeRequest()
    
    def __init__(self):
        # There always needs to be a value for the league
        self.league = "Standard"

    def print_query(self):
    	print(self.searchParams.query)
        

#PoeTradeObj = PoeTrade()

#PoeTradeObj.searchParams.query.name = "The Pariah"
#PoeTradeObj.searchParams.query.status.option = "online"

#stats = PoeRequest.Stats()
#stats.type = "and"
#stat_filter = PoeRequest.StatFilter()
#stat_filter.id = "my nuts"
#stat_filter.value.min = 1
#stat_filter.value.max = 10

#stats.filters.extend([stat_filter])

#PoeTradeObj.stats.extend([stats])

#PoeTradeObj.print_query()
