class PlayerStats():
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        def f(arg):
            return arg.nationality==nationality
        arr = list(filter(f, self.players))
        j = sorted(arr, key=lambda x: int(x.assists)+int(x.goals), reverse=True)
        return j

