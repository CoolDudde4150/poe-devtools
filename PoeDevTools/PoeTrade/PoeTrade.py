import json
import requests
import request_pb2 as query
from google.protobuf.json_format import MessageToJson, MessageToDict

class PoeTrade:
    URL = "https://www.pathofexile.com/api/trade/search/"
    
    def __init__(self):
        # There always needs to be a value for the league
        self.league = "Standard"
        


PARAMS = {
    "query": {
        "status": {
            "option": "online"
        },
        "name": "The Pariah",
        "type": "Unset Ring",
        "stats": [{
            "type": "and",
            "filters": []
        }]
    },
    "sort": {
        "price": "asc"
    }
}

b = query.PoeTradeRequest()

b.query.status.option = "online"
b.query.name = "The Pariah"
b.query.type = "Unset Ring"
b.query.stats.extend([])

print((MessageToDict(b, True)))

response = requests.post("https://www.pathofexile.com/api/trade/search/Standard", json = MessageToDict(b, True))

cool = response.json()
print(cool)