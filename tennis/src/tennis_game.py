class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0
        self.score_map = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_equal_score(self):
        if not self.m_score1 in self.score_map:
            score = "Deuce"
            return score
        return self.score_map[self.m_score1]+"-All"

    def get_advantage_score(self):
        minus_result = self.m_score1 - self. m_score2
        advantage_map = {
            -1: "Advantage player2",
            1: "Advantage player1"
        }
        if minus_result in advantage_map:
            return advantage_map[minus_result]
        elif minus_result>=2:
            return "Win for player1"
        return "Win for player2"
    
    def get_other_score(self):
        score = ""
        temp_score = 0
        for i in range(1, 3):
            if i == 1:
                temp_score = self.m_score1
            else:
                score = score + "-"
                temp_score = self.m_score2
            score+=self.score_map[temp_score]
        return score

    def get_score(self):

        if self.m_score1 == self.m_score2:
            return self.get_equal_score()

        elif self.m_score1 >= 4 or self.m_score2 >= 4:
            return self.get_advantage_score()

        return self.get_other_score()

