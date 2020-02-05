import os
import sys 

from poedevtools.trade import PoeTrade

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def test_malformed_search():
    """Tests the ability to handle malformed searches
    """
    trade_obj = PoeTrade.PoeTrade()

    request = trade_obj.query
    request.query.status.option = "Definitely not online ;)"

    # Expected error
    unknown_status_error = {"error": {"code": 2, "message": "Unknown status type"}}

    assert trade_obj.search(query=request) == unknown_status_error


def test_empty_search():
    """Tests the PoeTrade object's response to an empty query
    """
    trade_obj = PoeTrade.PoeTrade()
    trade_obj.reset_query()

    # Expected error
    query_missing_error = {"error": {"code": 2, "message": "Query missing."}}

    assert trade_obj.search(query=None) == query_missing_error
    assert trade_obj.search() == query_missing_error


def test_query_datatypes():
    """Tests the PoeTrade object's ability to search with various json formats. 

    """
    trade_obj = PoeTrade.PoeTrade()

    proto_request = trade_obj.query

    proto_request.query.status.option = "online"
    proto_request.sort.price = "dsc"
    proto_request.query.name = "Bottled Faith"
    
    dict_request = {"query": {"status": {"option":"online"}, "name": "Bottled Faith"}, "sort": {"price": "dsc"}}
    json_request = '''{
    "query": {
        "status": {
            "option": "online"
        },
        "name": "Bottled Faith"
    },
    "sort": {
        "price": "dsc"
    }
}'''

    proto_response = trade_obj.search(proto_request, num_get=1)
    dict_response = trade_obj.search(dict_request, num_get=1)
    json_response = trade_obj.search(json_request, num_get=1)

    assert (proto_response == dict_response) and (dict_response == json_response) and (json_response == proto_response)

def test_get_leagues():
    trade_obj = PoeTrade.PoeTrade()

    # Assert that there is at least one league returned.
    assert len(trade_obj.get_leagues()) > 0

def test_num_get_trade_search():
    trade_obj = PoeTrade.PoeTrade()
    query = trade_obj.query

    query.query.status.option = "online"

    assert len(trade_obj.search(query)["result"]) == 10
    assert len(trade_obj.search(query, num_get=11)["result"]) == 11
    assert len(trade_obj.search(query, num_get=22)["result"]) == 22
    assert len(trade_obj.search(query, num_get=6)["result"]) == 6