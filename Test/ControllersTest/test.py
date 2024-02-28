import unittest
from io import StringIO
from unittest.mock import patch, MagicMock
from Controllers.MatchController import MatchController
from Controllers.MenuController import MenuController
from Controllers.PlayerController import PlayerController
from Controllers.ReportController import ReportController
from Controllers.RoundsController import RoundsController
from Controllers.TournamentController import TournamentController


class TestMatchController(unittest.TestCase):
    def setUp(self):
        self.matchController = MatchController()

    def test_create_match_pairs(self):
        players = ['Player1', 'Player2', 'Player3', 'Player4']
        expected_pairs = [('Player1', 'Player2'), ('Player3', 'Player4')]
        self.assertEqual(self.matchController.create_match_pairs(players), expected_pairs)

    def test_has_played_together(self):
        player1 = {'first_name': 'John', 'last_name': 'Doe'}
        player2 = {'first_name': 'Jane', 'last_name': 'Doe'}
        played_matches = [[('John Doe', 1), ('Jane Doe', 0.5)]]
        self.assertTrue(self.matchController.has_played_together(player1, player2, played_matches))


class TestMenuController(unittest.TestCase):

    def setUp(self):
        self.menuController = MenuController()

    @patch('builtins.input', side_effect=['1', '0'])
    def test_user_choice_add_player(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.menuController.user_choice()
            self.assertEqual(fake_out.getvalue().strip(), "Au revoir!")

    def test_report_menu_choice_1(self):
        with patch('builtins.input', return_value='1'), \
             patch('sys.stdout', new=StringIO()) as fake_out:
            self.menuController.report_menu_choice()
            self.assertTrue("Affichage des joueurs par ordre alphabétique" in fake_out.getvalue().strip())


class TestPlayerController(unittest.TestCase):

    @patch('builtins.input', side_effect=['John', 'Doe', '01/01/1990', 'AB12345'])
    def test_add_player(self, mock_input):
        player_controller = PlayerController()
        player_controller.add_player()
        self.assertEqual(player_controller.first_name, 'John')
        self.assertEqual(player_controller.last_name, 'Doe')
        self.assertEqual(player_controller.birth_date, '01/01/1990')
        self.assertEqual(player_controller.national_chess_id, 'AB12345')

        self.assertTrue(player_controller.playerView.get_player_info.called)

        self.assertTrue(player_controller.player.save_player.called)

        self.assertIn('Joueur ajouté à la base de donnée avec succès !', 
                      player_controller.player.save_player.call_args.args[0])


class TestReportController(unittest.TestCase):

    def setUp(self):
        self.report_controller = ReportController()

    @patch('builtins.input', side_effect=['2'])  
    def test_select_tournament_from_list(self, mock_input):
        selected_tournament = self.report_controller.select_tournament_from_list()

        self.assertEqual(selected_tournament["name"], "Tournament 2")
        self.assertEqual(selected_tournament["id"], 2)


class TestRoundsController(unittest.TestCase):

    def setUp(self):
        self.rounds_controller = RoundsController()

    def test_shuffle_players_randomly(self):
        players = [{'name': 'Player1'}, {'name': 'Player2'}, {'name': 'Player3'}, {'name': 'Player4'}]
        shuffled_players = self.rounds_controller.shuffle_players_randomly(players)

        self.assertEqual(len(players), len(shuffled_players))

        self.assertNotEqual(players, shuffled_players)


class TestTournamentController(unittest.TestCase):

    def setUp(self):
        self.tournament_controller = TournamentController()

    @patch('builtins.input', side_effect=['Tournoi test', 'Location test', '2024-01-01',
                                          '2024-01-05', 5, 'Description test'])
    def test_create_tournament(self, mock_input):
        self.tournament_controller.create_tournament()
        self.assertTrue(self.tournament_controller.tournament.save_tournament.called)

    @patch('builtins.input', side_effect=[1])
    def test_add_player_to_tournament_success(self, mock_input):
        tournament_data = {
            'id': 1,
            'name': 'Tournoi test',
            'rounds': 2,
            'player_list': []
        }
        player_data = {
            'id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            'birth_date': '1990-01-01',
            'national_chess_id': '123456'
        }
        self.tournament_controller.tournament.get_tournaments = MagicMock(return_value=[tournament_data])
        self.tournament_controller.player.get_players = MagicMock(return_value=[player_data])
        self.tournament_controller.playerView.select_player = MagicMock(return_value=0)
        self.tournament_controller.tournament.update_tournament = MagicMock()

        self.tournament_controller.add_player_to_tournament()

        self.assertEqual(len(self.tournament_controller.tournament.update_tournament.call_args_list), 1)

    @patch('builtins.input', side_effect=[1])
    def test_add_player_to_tournament_duplicate(self, mock_input):
        tournament_data = {
            'id': 1,
            'name': 'Tournoi test',
            'rounds': 2,
            'player_list': [{'id': 1}]
        }
        player_data = {
            'id': 1,
            'first_name': 'John',
            'last_name': 'Doe',
            'birth_date': '1990-01-01',
            'national_chess_id': '123456'
        }
        self.tournament_controller.tournament.get_tournaments = MagicMock(return_value=[tournament_data])
        self.tournament_controller.player.get_players = MagicMock(return_value=[player_data])
        self.tournament_controller.playerView.select_player = MagicMock(return_value=0)
        self.tournament_controller.tournament.update_tournament = MagicMock()

        self.tournament_controller.add_player_to_tournament()

        self.assertEqual(len(self.tournament_controller.tournament.update_tournament.call_args_list), 0)


if __name__ == '__main__':
    unittest.main()
