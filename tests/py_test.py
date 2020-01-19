import pytest

import os
import sys

module_dir = os.path.dirname(__file__)
sys.path.append(os.path.join(module_dir, '../'))

from PoeDevTools.PoeTrade import PoeTrade

def test():
    assert True