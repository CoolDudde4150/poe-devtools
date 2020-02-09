import poedevtools.trade.PoeTrade as PoeTrade
import poedevtools.trade.trade_request_pb2 as TradeRequest

def test_imports():
    assert True

def test_blank_proto():
    trade_obj = PoeTrade.PoeTrade()

    empty_trade_query = TradeRequest.PoeTradeRequest()

    assert trade_obj.query == empty_trade_query

def test_cookie_maker():
    trade_obj = PoeTrade.PoeTrade()
    poesessid = "lolxd"

    expected_cookie = {"POESESSID": poesessid}

    assert trade_obj._populate_trade_cookie(poesessid) == expected_cookie

def test_dict_conversion():
    trade_obj = PoeTrade.PoeTrade()

    proto_query = trade_obj.query
    dict_query = {}
    json_query = '{"big fake": 123}'

    assert isinstance(PoeTrade.PoeTrade._convert2dict(proto_query), dict)
    assert isinstance(PoeTrade.PoeTrade._convert2dict(dict_query), dict)
    assert isinstance(PoeTrade.PoeTrade._convert2dict(json_query), dict)
    
def test_fetch_url_maker():
    results = []
    for i in range(10):
        results.append("%d" % i)

    expected_fetch_url = "https://www.pathofexile.com/api/trade/fetch/"
    for i in results:
        expected_fetch_url += i + ","
    expected_fetch_url = expected_fetch_url[:-1] + "?query=iden"

    assert PoeTrade.PoeTrade._get_fetch_url(results, "iden") == expected_fetch_url