import poedevtools.trade.PoeTrade as PoeTrade

def test_imports():
    assert True

def test_blank_proto():
    trade_obj = PoeTrade.PoeTrade()

    assert trade_obj.print_query() == None