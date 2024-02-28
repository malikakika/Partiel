from Models.Match import Match

class MatchController:

    def __init__(self):
        pass

    def create_match_pairs(self, players):
        """
        Divise une liste de joueurs en paires.

        Args:
            players (list): Une liste de joueurs.

        Returns:
            list: Une liste de paires de joueurs.
        """
        return list(zip(players[::2], players[1::2]))

    def create_matches(self, pairs):
        """
        Crée une liste de matches à partir d'une liste de paires de joueurs.

        Args:
            pairs (list): Une liste de paires de joueurs.

        Returns:
            list: Une liste de matches.
        """
        matches = []
        for player1, player2 in pairs:
            match = Match(player1, player2)
            matches.append(match)
        return matches

    def pair_players(self, sorted_players, played_matches):
        """
        Appaire les joueurs pour un match, en veillant à ce qu'ils n'aient pas joué ensemble.

        Args:
            sorted_players (list): Une liste de joueurs triée par score.
            played_matches (list): Une liste des matches joués précédemment.

        Returns:
            list: Une liste de paires de joueurs pour le prochain match.
        """
        paired_players = []
        unpaired_players = sorted_players.copy()

        while unpaired_players:
            player1 = unpaired_players.pop(0)
            opponent_found = False

            # Essayer de trouver un adversaire qu'il n'a pas encore rencontré
            for idx, potential_opponent in enumerate(unpaired_players):
                if not self.has_played_together(player1, potential_opponent, played_matches):
                    paired_players.append((player1, potential_opponent))
                    unpaired_players.pop(idx)
                    opponent_found = True
                    break

            # Si tous les adversaires potentiels ont déjà été rencontrés,
            # choisissez le premier non appairé comme adversaire
            if not opponent_found and unpaired_players:
                paired_players.append((player1, unpaired_players.pop(0)))

        return paired_players

    def has_played_together(self, player1, player2, played_matches):
        """
        Vérifie si deux joueurs ont déjà joué ensemble dans une liste de matches joués.

        Args:
            player1 (dict): Premier joueur.
            player2 (dict): Deuxième joueur.
            played_matches (list): Une liste des matches joués précédemment.

        Returns:
            bool: True si les joueurs ont déjà joué ensemble, sinon False.
        """
        player1_name = player1['first_name'] + ' ' + player1['last_name']
        player2_name = player2['first_name'] + ' ' + player2['last_name']

        for match in played_matches:
            players_in_match = [m[0] for m in match]
            if player1_name in players_in_match and player2_name in players_in_match:
                return True
        return False