import unittest
from io import StringIO
from unittest.mock import patch
from Views.MatchView import MatchView
from Views.RoundsView import RoundsView

class TestMatchView(unittest.TestCase):
    def setUp(self):
        self.matchView = MatchView()

    @patch('builtins.input', side_effect=['1'])
    def test_get_user_choice_valid_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            choice = self.matchView.get_user_choice()
            self.assertEqual(choice, 1)
            self.assertEqual(fake_out.getvalue().strip(), "Entrez votre choix (1, 2 ou 3): ")

    @patch('builtins.input', side_effect=['4', '2'])
    def test_get_user_choice_invalid_then_valid_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            choice = self.matchView.get_user_choice()
            self.assertEqual(choice, 2)
            self.assertIn("Choix invalide. Veuillez entrer 1, 2 ou 3.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=['abc', '1'])
    def test_get_user_choice_invalid_then_valid_string_input(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            choice = self.matchView.get_user_choice()
            self.assertEqual(choice, 1)
            self.assertIn("Entrée invalide. Veuillez entrer un numéro.", fake_out.getvalue().strip())

    @patch('builtins.input', side_effect=['1'])
    def test_display_match_results(self, mock_input):
        match = {'player1': {'first_name': 'John', 'last_name': 'Doe'}, 'player2': {'first_name': 'Jane', 'last_name': 'Doe'}}
        with patch('sys.stdout', new=StringIO()) as fake_out:
            user_choice = self.matchView.display_match_results(match, 1, 2)
            self.assertEqual(user_choice, 1)
            expected_output = "Match 1 Round 2 - Résultats\n1 - John Doe\n2 - Jane Doe\n3 - égalité"
            self.assertEqual(fake_out.getvalue().strip(), expected_output)
class TestRoundsView(unittest.TestCase):
    def setUp(self):
        self.roundsView = RoundsView()

    @patch('builtins.input', return_value='o')
    def test_ask_for_next_round_yes(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            response = self.roundsView.ask_for_next_round()
            self.assertEqual(response, 'o')
            self.assertEqual(fake_out.getvalue().strip(), "Voulez-vous passer au round suivant ? o/n: ")

    @patch('builtins.input', return_value='n')
    def test_ask_for_next_round_no(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            response = self.roundsView.ask_for_next_round()
            self.assertEqual(response, 'n')
            self.assertEqual(fake_out.getvalue().strip(), "Voulez-vous passer au round suivant ? o/n: ")

    @patch('builtins.input', return_value='O')
    def test_ask_for_next_round_uppercase_yes(self, mock_input):
        response = self.roundsView.ask_for_next_round()
        self.assertEqual(response, 'o')

    @patch('builtins.input', return_value='N')
    def test_ask_for_next_round_uppercase_no(self, mock_input):
        response = self.roundsView.ask_for_next_round()
        self.assertEqual(response, 'n')


if __name__ == '__main__':
    unittest.main()
