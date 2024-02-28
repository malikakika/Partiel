from Models.Report import Report


class ReportController:
    def __init__(self):
        pass

    def players_alphabetical(self):
        """
        Charge la liste des joueurs et les trie par ordre alphabétique de nom puis de prénom.

        Returns:
            list: Liste des joueurs triés par ordre alphabétique.
        """
        report = Report()
        players = report.load_players()
        sorted_players = sorted(players, key=lambda x: (x['last_name'], x['first_name']))
        return sorted_players

    def list_tournaments(self):
        """
        Charge et retourne la liste des tournois depuis le modèle de rapport.

        Returns:
            list: Liste des tournois.
        """
        report = Report()
        return report.load_tournaments()

    def select_tournament_from_list(self):
        """
        Affiche la liste des tournois et demande à l'utilisateur de sélectionner un tournoi par son numéro.

        Returns:
            dict: Le tournoi sélectionné.
        """
        report = Report()
        tournaments = report.load_tournaments()

        for i, tournament in enumerate(tournaments):
            print(f"{i + 1}. {tournament['name']}")

        while True:
            try:
                choice = int(input("\nSélectionnez un tournoi par son numéro : "))
                if 1 <= choice <= len(tournaments):
                    return tournaments[choice - 1]
                else:
                    print("Veuillez choisir un numéro valide.")
            except ValueError:
                print("Veuillez choisir un numéro valide.")

    def tournament_players_alphabetical(self):
        """
        Charge la liste des joueurs pour un tournoi spécifique,
          triée par ordre alphabétique de nom puis de prénom.

        Returns:
            list: Liste des joueurs du tournoi triés par ordre alphabétique.
        """
        tournament = self.select_tournament_from_list()
        players = tournament['player_list']
        sorted_players = sorted(players, key=lambda x: (x['last_name'], x['first_name']))
        return sorted_players

    def get_tournament_rounds_and_matches(self):
        """
        Sélectionne un tournoi et retourne son nom, la liste de ses tours et son ID.

        Returns:
            tuple: Tuple contenant le nom du tournoi, la liste de ses tours et son ID.
        """
        tournament = self.select_tournament_from_list()
        return tournament['name'], tournament['round_list'], tournament['id']

    def get_tournament_players_sorted(self, tournament_id):
        """
        Charge et retourne la liste des joueurs pour un tournoi spécifié,
        triée par leur score en ordre décroissant.

        Args:
            tournament_id (int): L'ID du tournoi dont on souhaite obtenir la liste des joueurs.

        Returns:
            list: Liste des joueurs du tournoi triés par score en ordre décroissant.
        """
        report = Report()
        tournaments = report.load_tournaments()

        for tournament in tournaments:
            if tournament["id"] == tournament_id:
                return sorted(tournament["player_list"], key=lambda x: x["score"], reverse=True)
        return []
