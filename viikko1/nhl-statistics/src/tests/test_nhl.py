import unittest
from player import Player
from statistics_service import StatisticsService, SortBy

SAMPLE = [
    Player("player a", "ABC", 2, 5),
    Player("player b", "ABC", 7, 3),
    Player("player c", "DEF", 3, 10),
    Player("player d", "GHI", 10, 2),
]


class MockPlayerReader:
    def __init__(self, players):
        self.players = players

    def get_players(self):
        return self.players


class TestPlayer(unittest.TestCase):
    def test_str(self):
        self.assertEqual(str(SAMPLE[0]), "player a ABC 2 + 5 = 7")


class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        self.stats = StatisticsService(MockPlayerReader(SAMPLE))

    def test_search(self):
        self.assertEqual(self.stats.search("player a"), SAMPLE[0])
        self.assertEqual(self.stats.search("player e"), None)

    def test_team(self):
        self.assertEqual(self.stats.team("ABC"), SAMPLE[:2])
        self.assertEqual(self.stats.team("JKL"), [])

    def test_top(self):
        def players(list, indices):
            ans = []
            for idx in indices:
                ans.append(list[idx])
            return ans

        self.assertEqual(self.stats.top(2, SortBy.POINTS), players(SAMPLE, [2, 3, 1]))
        self.assertEqual(self.stats.top(2), players(SAMPLE, [2, 3, 1]))
        self.assertEqual(self.stats.top(2, SortBy.GOALS), players(SAMPLE, [3, 1, 2]))
        self.assertEqual(self.stats.top(2, SortBy.ASSISTS), players(SAMPLE, [2, 0, 1]))
