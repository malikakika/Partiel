from Controllers.PlayerController import PlayerController
from Controllers.TournamentController import TournamentController
from Controllers.RoundsController import RoundsController
from Controllers.ReportController import ReportController
from Views.ReportView import ReportView
from Views.Menu import Menu


class MenuController:
    def __init__(self):
        self.menu = Menu()
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.rounds_controller = RoundsController()
        self.report_controller = ReportController()
        self.report_view = ReportView()

    def user_choice(self):
        """
        Gère le choix de l'utilisateur dans le menu principal et appelle les fonctions correspondantes.
        """
        choice = self.menu.main_menu()

        match choice:
            case '1':
                self.player_controller.add_player()
                self.user_choice()
            case '2':
                self.tournament_controller.create_tournament()
                self.user_choice()
            case '3':
                self.tournament_controller.add_player_to_tournament()
                self.user_choice()
            case '4':
                self.rounds_controller.play_round()
                self.user_choice()
            case '5':
                self.report_menu_choice()
                self.user_choice()
            case '0':
                print("Au revoir!")
                exit()
            case _:
                print("Choix non valide. Veuillez entrer un chiffre valide.")
                self.user_choice()

    def report_menu_choice(self):
        """
        Gère le choix de l'utilisateur dans le sous-menu des rapports et
        appelle les méthodes correspondantes.
        """
        choice = self.menu.report_menu()

        match choice:
            case '1':
                players = self.report_controller.players_alphabetical()
                self.report_view.display_players_alphabetical(players)
            case '2':
                tournaments = self.report_controller.list_tournaments()
                self.report_view.display_tournaments(tournaments)
            case '3':
                selected_tournament = self.report_controller.select_tournament_from_list()
                self.report_view.display_tournament_infos(selected_tournament)
            case '4':
                players = self.report_controller.tournament_players_alphabetical()
                self.report_view.display_tournament_players_alphabetical(players)
            case '5':
                (tournament_name,
                 rounds_list,
                 tournament_id) = (
                    self.report_controller.get_tournament_rounds_and_matches())
                players_sorted = (
                    self.report_controller.get_tournament_players_sorted(tournament_id))
                self.report_view.display_rounds_and_matches(tournament_name, rounds_list, players_sorted)
            case '0':
                return  # MAIN MENU
            case _:
                print("Choix non valide. Veuillez entrer un chiffre valide.")
                self.report_menu_choice()
