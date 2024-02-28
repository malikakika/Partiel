from Views.View import View


class PlayerView(View):

    def __init__(self):
        self.national_chess_id = None
        self.birth_date = None
        self.last_name = None
        self.first_name = None

    def get_player_info(self):
        """
        Récupère et valide les informations du joueur telles que le prénom, le nom,
        la date de naissance et l'identifiant national d'échecs.

        Returns:
            tuple: Un tuple contenant le prénom, le nom, la date de naissance
            et l'identifiant national d'échecs du joueur.
        """
        self.first_name = self.get_valid_alpha_input("Prénom: ")
        self.last_name = self.get_valid_alpha_input("Nom de famille: ")

        # Appel de la méthode présente dans View.py
        self.birth_date = self.get_valid_date_input("Date de naissance (JJ/MM/AAAA): ")

        while True:
            self.national_chess_id = input("Identifiant national d'échecs (AB12345, optionnel) : ")
            if self.national_chess_id:  # si l'utilisateur a entré quelque chose
                if not self.is_valid_id(self.national_chess_id):
                    print("Identifiant national d'échecs invalide. Réessayez.")
                else:
                    break
            else:
                break

        return self.first_name, self.last_name, self.birth_date, self.national_chess_id

    def select_player(self, players):
        """
        Permet à l'utilisateur de sélectionner un joueur parmi une liste de joueurs.

        Args:
            players (list): Liste des joueurs.

        Returns:
            int: L'indice du joueur sélectionné dans la liste.
        """
        print("\nSélectionnez un joueur : ")
        players_reversed = list(reversed(players))
        for i, player in enumerate(players_reversed):
            print(
                    f"{i + 1} - {player['first_name']} {player['last_name']} - Né le {player['birth_date']} "
                    f"- ID: {player['national_chess_id']}"
                  )

        while True:
            try:
                player_index = int(input("\nEntrez le numéro du joueur que vous voulez sélectionner : ")) - 1
                if player_index < 0 or player_index >= len(players_reversed):
                    print("Numéro de joueur invalide. Veuillez entrer un numéro de joueur valide.")
                else:
                    return len(players) - 1 - player_index
            except ValueError:
                print("Entrée invalide. Veuillez entrer un numéro.")
