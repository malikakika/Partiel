from Models.Player import Player
from Models.Tournament import Tournament
from Views.TournamentView import TournamentView
from Views.PlayerView import PlayerView


class TournamentController:
    def __init__(self):
        self.tournament = Tournament(None, None, None, None, None, None)
        self.player = Player(None, None, None, None)
        self.tournamentView = TournamentView()
        self.playerView = PlayerView()

    def create_tournament(self):
        """
        Crée un tournoi en récupérant les informations nécessaires depuis la vue du tournoi,
        puis le sauvegarde.
        """
        name, location, start_date, end_date, rounds, description = self.tournamentView.get_tournament_info()
        self.tournament = (
            Tournament(name=name,
                       location=location,
                       start_date=start_date,
                       end_date=end_date,
                       rounds=rounds,
                       current_round=1,
                       description=description))
        self.tournament.save_tournament()

    def add_player_to_tournament(self):
        """
        Permet d'ajouter un joueur à un tournoi spécifique.
        - Récupère la liste des tournois et des joueurs
        - Demande à l'utilisateur de choisir un tournoi
        - Vérifie que le tournoi choisi n'est pas complet
        - Demande à l'utilisateur de choisir un joueur à ajouter
        - Ajoute le joueur au tournoi et met à jour le fichier JSON
        """
        # Récupérer tous les tournois
        tournaments = self.tournament.get_tournaments()
        # Récupérer tous les joueurs
        players = self.player.get_players()

        # Afficher tous les tournois et demander à l'utilisateur d'en choisir un
        selected_tournament_id = self.tournamentView.select_tournament(tournaments)

        selected_tournament = None
        for tournament in tournaments:
            if tournament['id'] == selected_tournament_id:
                selected_tournament = tournament
                break

        if selected_tournament is None:
            print('Tournoi introuvable')
            return

        # Verification de tournoi complet
        registered_players = len(selected_tournament['player_list'])
        max_players = selected_tournament['rounds'] * 2
        print(f"registered_players = {registered_players}")
        print(f"max_players = {max_players}")
        if registered_players >= max_players:
            print('Le tournoi est complet.')
            return

        # Boucle pour la sélection du joueur
        while True:
            # Afficher tous les joueurs et demander à l'utilisateur d'en choisir un
            player_index = self.playerView.select_player(players)
            if player_index is not None:
                selected_player = players[player_index]

                # Ajouter le joueur sélectionné au tournoi
                if selected_player['id'] in [player['id'] for player in selected_tournament['player_list']]:
                    print('Joueur déjà enregistré pour ce tournoi')
                else:
                    selected_player['score'] = 0
                    selected_tournament['player_list'].append(selected_player)

                    # Mettre à jour le tournoi dans le fichier JSON
                    self.tournament.update_tournament(selected_tournament)

                    # Demander à l'utilisateur s'il souhaite ajouter un autre joueur
                    add_another = input("Souhaitez-vous ajouter un nouveau joueur à ce tournoi ? o/n: ")
                    if add_another.lower() != 'o':
                        break  # Sortir de la boucle après avoir ajouté le joueur
