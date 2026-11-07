import unittest
from player import Player
from player_stats import PlayerStats


class StubReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestPlayerStats(unittest.TestCase):
    def setUp(self):
        players = [
            Player(
                {
                    "name": "Alex",
                    "team": "AAA",
                    "goals": 10,
                    "assists": 20,
                    "nationality": "FIN",
                }
            ),
            Player(
                {
                    "name": "Ben",
                    "team": "BBB",
                    "goals": 15,
                    "assists": 5,
                    "nationality": "CAN",
                }
            ),
            Player(
                {
                    "name": "Chris",
                    "team": "AAA",
                    "goals": 8,
                    "assists": 12,
                    "nationality": "CAN",
                }
            ),
        ]
        self.stats = PlayerStats(StubReader(players))

    def test_top_scorers_by_nationality_returns_players_in_points_order(self):
        players = self.stats.top_scorers_by_nationality("CAN")

        self.assertEqual(["Ben", "Chris"], [player.name for player in players])
        self.assertEqual([20, 20], [player.points for player in players])

    def test_top_scorers_by_nationality_returns_empty_list_for_unknown_nationality(
        self,
    ):
        self.assertEqual([], self.stats.top_scorers_by_nationality("SWE"))

    def test_top_scorers_by_team_returns_matching_players_in_points_order(self):
        players = self.stats.top_scorers_by_team("AAA")

        self.assertEqual(["Alex", "Chris"], [player.name for player in players])
        self.assertEqual([30, 20], [player.points for player in players])

    def test_top_goal_scorers_returns_requested_number_in_goal_order(self):
        players = self.stats.top_goal_scorers(2)

        self.assertEqual(["Ben", "Alex"], [player.name for player in players])
        self.assertEqual([15, 10], [player.goals for player in players])
