import sys
import requests
from player import Player


class PlayerReader:
    def __init__(self, url, console):
        self._url = url
        self.console = console

    def get_players(self):
        res = requests.get(self._url).json()
        if isinstance(res, dict) and res.get("error"):
            self.console.print(f"[red]Error: {res["error"]}")
            sys.exit()
        return [Player(player_dict) for player_dict in res]
