import pytest

import os
import sys

import sys, os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from poedevtools.trade import PoeTrade

import numpy



def test_imports():
    assert True

def test_blank_proto():
    trade_obj = PoeTrade.PoeTrade()

    assert trade_obj.print_query() == None

def test_malformed_search():
    trade_obj = PoeTrade.PoeTrade()

    request = trade_obj.get_query()
    request.query.status.option = "Definitely not online ;)"

    assert trade_obj.search(PoeTradeRequest=request) == None

def test_empty_search():
    trade_obj = PoeTrade.PoeTrade()
    
    assert trade_obj.search(PoeTradeRequest=None) == None
    assert trade_obj.search() == None