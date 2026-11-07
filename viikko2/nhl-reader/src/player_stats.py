class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nat):
        temp = [player for player in self._players if player.nationality == nat]
        return sorted(temp, key=lambda x: x.points, reverse=True)

    def top_scorers_by_team(self, team):
        temp = [player for player in self._players if player.teams == team]
        return sorted(temp, key=lambda x: x.points, reverse=True)

    def top_goal_scorers(self, how_many):
        """Palauttaa how_many eniten maaleja tehnyttä pelaajaa
        maalimäärän mukaan laskevassa järjestyksessä"""
        return sorted(self._players, key=lambda x: x.goals, reverse=True)[:how_many]
