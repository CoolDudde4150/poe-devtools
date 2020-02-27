"""Functionality to interact with the Poe.Watch api in a standard way

Provides:
    * Access to all api endpoints with simple functions.
    * Thats it. Its just an interface lol

More documentation can be found at https://poe.watch/api
"""

import requests


class PoeWatchAPI:
    """Provides an interface to the Poe.Watch API.
    """

    def __init__(self):
        self._poewatch_api_startpoint = "https://api.poe.watch/"

    def _make_query(self, endpoint, params=None):
        return requests.get(self._poewatch_api_startpoint + endpoint, params=params)

    def get_latest_change_id(self):
        return self._make_query("id")

    def get_leagues(self):
        return self._make_query("leagues")

    def get_item_info(self):
        return self._make_query("itemdata")

    def get_character_names(self, account_name):
        json = {"account": account_name}

        return self._make_query("characters", params=json)

    def get_categories(self):
        return self._make_query("categories")

    def get_category_data(self, league, category):
        json = {"league": league, "category": category}

        return self._make_query("get", params=json)

    def get_compact_data(self, league):
        json = {"league": league}

        return self._make_query("compact", params=json)

    def get_item_data(self, iden):
        json = {"id": iden}

        return self._make_query("item", params=json)

    def get_item_history(self, iden, league):
        json = {"id": iden, "league": league}

        return self._make_query("itemhistory", params=json)

    def get_item_listings(self, league, account):
        json = {"league": league, "account": account}

        return self._make_query("listings", params=json)
