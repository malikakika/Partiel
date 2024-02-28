from random import shuffle
from Models.Tournament import Tournament
from Controllers.MatchController import MatchController
from Views.TournamentView import TournamentView
from Views.MatchView import MatchView
from Views.RoundsView import RoundsView
import json


class RoundsController:
    def __init__(self):
        self.tournament = Tournament(None, None, None, None, None, None)
        self.tournamentView = TournamentView()
        self.matchController = MatchController()
        self.matchView = MatchView()
        self.roundsView = RoundsView()
    def shuffle_players_randomly(self, players):
        """
        Mélange la liste des joueurs de manière aléatoire.

        Args:
            players (list): Liste des joueurs à mélanger.

        Returns:
            list: Liste des joueurs mélangés.
        """
        shuffle(players)
        return players
        

    def sort_players_by_score(self, players):
        """
        Trie les joueurs par score, et mélange aléatoirement ceux ayant le même score.

        Args:
            players (list): Liste des joueurs à trier.

        Returns:
            list: Liste des joueurs triés par score.
        """
        scores = set(player['score'] for player in players)
        sorted_players = []
        for score in sorted(scores, reverse=True):
            players_with_same_score = [p for p in players if p['score'] == score]
            shuffle(players_with_same_score)
            sorted_players.extend(players_with_same_score)
        return sorted_players

    def load_tournaments(self):
        """
        Charge et retourne la liste des tournois depuis un fichier JSON.

        Returns:
            list: Liste des tournois ou une liste vide en cas d'erreur.
        """
        try:
            with open('data/tournaments.json', 'r') as f:
                tournaments = json.load(f)
            return tournaments
        except FileNotFoundError:
            print("Le fichier de tournois n'existe pas.")
            return []
        except json.JSONDecodeError:
            print("Erreur lors de la lecture du fichier JSON.")
            return []

    def get_match_results(self, matches, current_round):
        """
        Obtient les résultats des matchs pour un tour donné, à partir de l'entrée utilisateur.

        Args:
            matches (list): Liste des matchs à jouer pendant le tour.
            current_round (int): Numéro du tour actuel.

        Returns:
            list: Liste des résultats des matchs.
        """
        results = []
        for idx, match in enumerate(matches, start=1):
            user_choice = self.matchView.display_match_results(match, idx, current_round)

            player1_fullname = match.player1['first_name'] + ' ' + match.player1['last_name']
            player2_fullname = match.player2['first_name'] + ' ' + match.player2['last_name']

            if user_choice == 1:
                match_data = ([player1_fullname, 1], [player2_fullname, 0])
            elif user_choice == 2:
                match_data = ([player1_fullname, 0], [player2_fullname, 1])
            else:
                match_data = ([player1_fullname, 0.5], [player2_fullname, 0.5])

            results.append(match_data)

        return results

    def update_player_scores(self, selected_tournament, match_results):
        """
        Met à jour les scores des joueurs dans un tournoi sélectionné, en fonction des résultats des matchs.

        Args:
            selected_tournament (dict): Tournoi sélectionné.
            match_results (list): Résultats des matchs du tour.
        """
        for match in match_results:
            for player_data in match:
                player_fullname = player_data[0]
                score = player_data[1]
                for player in selected_tournament['player_list']:
                    if player['first_name'] + ' ' + player['last_name'] == player_fullname:
                        player['score'] += score
                        break

    def play_round(self):
        """
        Gère le déroulement d'un tour dans un tournoi,
        de la sélection du tournoi à la mise à jour des scores des joueurs.
        """
        tournaments = self.load_tournaments()
        if not tournaments:
            print("Pas de tournois disponibles.")
            return

        tournament_id = self.tournamentView.select_tournament(tournaments)

        # Charger le tournoi sélectionné
        selected_tournament = next((tournament for tournament in tournaments if tournament['id'] == tournament_id),
                                   None)
        if not selected_tournament:
            print("Tournoi non trouvé.")
            return

        if selected_tournament["current_round"] > selected_tournament["rounds"]:
            print("Tous les rounds du tournoi ont été joués. Le tournoi est terminé.")
            return

        print(f"Vous avez sélectionné le tournoi {selected_tournament['name']}.")

        if not selected_tournament['round_list']:
            players_for_round = self.shuffle_players_randomly(selected_tournament['player_list'])
        else:
            players_for_round = self.sort_players_by_score(selected_tournament['player_list'])

        pairs = self.matchController.create_match_pairs(players_for_round)
        matches = self.matchController.create_matches(pairs)

        if not selected_tournament['round_list']:
            current_round = 1
        else:
            last_round = selected_tournament["round_list"][-1]["Round"]
            current_round = last_round + 1

        print(f"Matches du Round {current_round}")
        for match in matches:
            print(match)

        match_results = self.get_match_results(matches, current_round)
        self.update_player_scores(selected_tournament, match_results)

        round_data = {
            "Round": current_round,
            "matches": match_results
        }
        selected_tournament['round_list'].append(round_data)
        selected_tournament["current_round"] += 1

        # Update the tournament data in the file
        self.tournament.update_tournament(selected_tournament)

        while True:
            user_choice = self.roundsView.ask_for_next_round()
            if user_choice == 'o':
                self.play_round()  # On rappelle la fonction en récursif
                break
            elif user_choice == 'n':
                break
            else:
                print("Réponse non reconnue. Veuillez répondre par 'o' ou 'n'.")
