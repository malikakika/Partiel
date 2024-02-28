import unittest
from Models.Match import Match

class TestMatch(unittest.TestCase):

    def setUp(self):
        self.player1 = {'first_name': 'John', 'last_name': 'Doe'}
        self.player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
        self.match = Match(self.player1, self.player2)

    def test_serialize(self):
        expected_serialization = {
            'player1': self.player1,
            'player2': self.player2,
            'winner': None
        }
        self.assertEqual(self.match.serialize(), expected_serialization)

    def test_str(self):
        expected_str = "John Doe VS Jane Doe"
        self.assertEqual(str(self.match), expected_str)

if __name__ == '__main__':
    unittest.main()
