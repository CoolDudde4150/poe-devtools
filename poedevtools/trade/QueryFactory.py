import poedevtools.trade.trade_request_pb2 as PoeQuery

from google.protobuf.json_format import MessageToDict

class TradeFactory:
    
    def _get_query(self, query):
        return MessageToDict(query)

    def _set_min_max(self, query, min, max):
        if min is not None:
            query.min = min
        if max is not None:
            query.max = max
    
    def _set_disabled(self, disabled, query):
        query.disabled = disabled

class QueryFactory(TradeFactory):

    def __init__(self):
        self.query = PoeQuery.PoeTradeRequest()
        self.stat_factory = StatFilterFactory()
        self.filter_factory = FilterFactory()

    def get_query(self):
        # Need a copy so that we can copy to it without repercussions
        query = self.query
        query.query.stats.append(self.stat_factory.stats)

        return self._get_query(query)
    
    def clear(self):
        self.query.Clear()
        
    def set_name(self, name):
        self.query.query.name = name
        return self

    def set_type(self, item_type):
        self.query.query.type = item_type
        return self
    
    def set_status(self, status):
        self.query.query.status.option = status
        return self


class StatFilterFactory(TradeFactory):
    def __init__(self):
        self.stat_filter = PoeQuery.StatFilter()
        self.stats = PoeQuery.Stats()

    def set_id(self, stat_id):
        self.stat_filter.id = stat_id
        return self
    
    def set_value_range(self, min=None, max=None):
        self._set_min_max(self.stat_filter.value, min, max)
        return self
        
    def set_disabled(self, disabled):
        self.stat_filter.disabled = disabled
        return self

    def set_type(self, search_type):
        self.stats.type = search_type
    
    def build(self):
        self.stats.filters.extend([self.stat_filter])



class FilterFactory(TradeFactory):
    def __init__(self):
        self.weapon_filter_factory = WeaponFilterFactory()


class WeaponFilterFactory(TradeFactory):
    def __init__(self):
        self.weapon_filter = PoeQuery.WeaponRequirements()

    def set_disabled(self, disabled):
        self.weapon_filter.disabled = disabled
    
    def set_damage_range(self, min=None, max=None):
        self._set_min_max(self.weapon_filter.filters.damage, min, max)

    def set_crit_range(self, min=None, max=None):
        self._set_min_max(self.weapon_filter.filters.crit, min, max)

    def set_aps_range(self, min=None, max=None):
        self._set_min_max(self.weapon_filter.filters.aps, min, max)
    
    def set_dps_range(self, min=None, max=None):
        self._set_min_max(self.weapon_filter.filters.dps, min, max)
    
    def set_edps_range(self, min=None, max=None):
        self._set_min_max(self.weapon_filter.filters.edps, min, max)
    
    def set_pdps_range(self, min=None, max=None):
        self._set_min_max(self.weapon_filter.filters.pdps, min, max)

    def get_query(self):
        return self._get_query(self.weapon_filter)