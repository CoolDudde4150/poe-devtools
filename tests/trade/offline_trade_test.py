import poedevtools.trade.PoeTrade as PoeTrade
import poedevtools.trade.trade_request_pb2 as TradeRequest

def test_imports():
    assert True

def test_blank_proto():
    trade_obj = PoeTrade.PoeTrade()

    empty_trade_query = TradeRequest.PoeTradeRequest()

    assert trade_obj.query == empty_trade_query