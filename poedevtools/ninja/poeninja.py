import requests

class PoeWatchAPI:
    poewatchAPI_startpoint = "https://api.poe.watch/"

    def __init__(self):
        pass

    def _make_query(self, endpoint, params=None):
        return requests.get(self.poewatchAPI_startpoint + endpoint, params = params)

    def get_latest_change_id(self):
        return self._make_query("id")

    def get_leagues(self):
        return self._make_query("leagues")
    
    def get_item_info(self):
        return self._make_query("itemdata")

    def get_character_names(self, account_name):
        json = {"account": account_name}

        return self._make_query("characters", params = json)

    def get_categories(self):
        return self._make_query("categories")

    def get_category_data(self, league, category):
        json = {"league": league,
                "category": category}
        
        return self._make_query("get", params = json)

    def get_compact_data(self, league):
        json = {"league": league}

        return self._make_query("compact", params = json)

    def get_item_data(self, id):
        json = {"id": id}

        return self._make_query("item", params = json)

    def get_item_history(self, id, league):
        json = {"id": id,
                "league": league}

        return self._make_query("itemhistory", params = json)

    def get_item_listings(self, league, account):
        json = {"league": league,
                "account": account}

        return self._make_query("listings", params = json)

    

    