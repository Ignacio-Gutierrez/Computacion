import unittest

def find_winners(self, scores):
    
    jumpFirstIteration = True
    winner = []

    for scoresKey in scores:
        if jumpFirstIteration == True:
            winner.append(scoresKey)
            jumpFirstIteration = False
        elif scores[winner[0]] < scores[winner]:
            winner = [scoresKey]
        elif scores[winner[0]] == scores[winner]:
            winner.append(scoresKey)
    return winner


class TestWinner(unittest.TestCase):
    def test_1(self):
        scores = {'Mary': 1000,'John': 200}
        winner = find_winners(scores)
        self.assertEqual(winner, ['Mary'])

    def test_2(self):
        scores = {'Mary': 1000,'John': 200,'Gabriel': 2000}
        winner = find_winners(scores)
        self.assertEqual(winner, ['Gabriel'])

if __name__ == '__main__':
    unittest.main()

