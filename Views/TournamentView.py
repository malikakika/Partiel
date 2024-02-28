from Views.View import View
class TournamentView(View):
    def __init__(self):
        self.description = None
        self.rounds = None
        self.end_date = None
        self.start_date = None
        self.location = None
        self.name = None

    def get_tournament_info(self):
        """
        Demande à l'utilisateur de fournir les informations pour un nouveau tournoi.
        Effectue des validations pour s'assurer que les entrées sont correctes.

        Returns:
            tuple: Tuple contenant les informations du tournoi
            (nom, lieu, date de début, date de fin, nombre de rounds, description).
        """
        self.name = self.get_valid_alpha_input("Nom du tournoi: ")
        self.location = self.get_valid_alpha_input("Lieu: ")

        # Appel de la méthode présente dans View.py
        self.start_date = self.get_valid_date_input("Date de début (JJ/MM/AAAA): ")
        self.end_date = self.get_valid_date_input("Date de fin (JJ/MM/AAAA): ")

        self.rounds = self.get_valid_int_input("Nombre de tours (optionnel, défaut à 4): ", 4)  # IF EMPTY, SET TO 4
        self.description = input("Description du tournoi (optionnel): ")

        return self.name, self.location, self.start_date, self.end_date, self.rounds, self.description

    def select_tournament(self, tournaments):
        """
        Affiche une liste de tournois existants et demande à l'utilisateur d'en sélectionner un.

        Args:
            tournaments (list): Liste des tournois existants.

        Returns:
            int: ID du tournoi sélectionné.
        """
        print("\nSélectionnez un tournoi : ")
        tournaments_reversed = list(reversed(tournaments))
        for i, tournament in enumerate(tournaments_reversed):
            registered_players = len(tournament['player_list'])
            print(
                f"{i + 1} - {tournament['name']} à {tournament['location']} du {tournament['start_date']} au {tournament['end_date']} - Rounds: {tournament['rounds']} - Inscrits: {registered_players}"
            )
        while True:
            try:
                tournament_index = int(input("\nEntrez le numéro du tournoi que vous voulez sélectionner : ")) - 1
                if tournament_index < 0 or tournament_index >= len(tournaments):
                    print("Numéro de tournoi invalide. Veuillez entrer un numéro de tournoi valide.")
                else:
                    # On retourne l'ID à ne pas confondre avec les options en affichage (pas les mêmes valeurs)
                    return tournaments_reversed[tournament_index]['id']
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")
