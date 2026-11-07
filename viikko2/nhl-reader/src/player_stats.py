class PlayerStats:
    def __init__(self, reader):
        self._players = reader.get_players()

    def top_scorers_by_nationality(self, nat):
        temp = [player for player in self._players if player.nationality == nat]
        return sorted(temp, key=lambda x: x.points, reverse=True)
