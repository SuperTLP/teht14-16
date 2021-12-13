class And:
    def __init__(self, *matchers):
        self._matchers = matchers
    
    def matches(self, player):
        for matcher in self._matchers:
            if not matcher.matches(player):
                return False
        
        return True

class PlaysIn:
    def __init__(self, query, team):
        self._team = team
        self.query=query

    def matches(self, player):
        return player.team == self._team

class HasAtLeast:
    def __init__(self, query, value, attr):
        self._value = value
        self._attr = attr
        self.query=query

    def matches(self, player):
        player_value = getattr(player, self._attr)

        return (player_value >= self._value and self.query.matches(player))

class All:
    def __init__(self, *matchers):
            self._matchers = matchers

    def matches(self, player):
        return True

class HasFewerThan:
    def __init__(self, query, value, attr):
        self._value=value
        self._attr=attr
        self.query=query
    def matches(self, player):
        player_value = getattr(player, self._attr)

        return (player_value < self._value and self.query.matches(player))

class Not:
    def __init__(self, query, *matchers):
        self._matchers = matchers
        self.query=query
    
    def matches(self, player):
        for matcher in self._matchers:
            if not self.query.matches(player) or matcher.matches(player):
                return False
        return True

class Or:
    def __init__(self, queries):
        self._queries=queries
    def matches(self, player):
        for i in self._queries:
            if i.matches(player):
                return True
        return False

class QueryBuilder:
    def __init__(self, query = All()):
        self.query=query
        pass
    def playsIn(self, team):
        return QueryBuilder(PlaysIn(self.query, team))
    def hasAtLeast(self, num, attr):
        return QueryBuilder(HasAtLeast(self.query, num, attr))
    def hasFewerThan(self, num, attr):
        return QueryBuilder(HasFewerThan(self.query, num, attr))
    def oneOf(self, *args):
        return QueryBuilder(Or(args))
    def build(self):
        return self.query