class Menu:
    def __init__(self):
        self.choice = None

    def main_menu(self):
        """
        Affiche le menu principal du gestionnaire de tournois d'échecs.

        Returns:
            str: Le choix de l'utilisateur pour le menu principal.
        """
        print("\n========CHESS TOURNAMENT MANAGER========")
        print("\n--- MENU ---")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Ajouter des joueurs à un tournoi")
        print("4. Lancer un Round")
        print("5. Rapports")
        print("0. Quitter")

        self.choice = input("\nEntrez le numéro correspondant à votre choix : ")

        return self.choice

    def report_menu(self):
        """
        Affiche le menu des rapports pour le gestionnaire de tournois d'échecs.

        Returns:
            str: Le choix de l'utilisateur pour le menu des rapports.
        """
        print("\nMenu des rapports:")
        print("1. Liste des joueurs par ordre alphabétique")
        print("2. Liste des tous les Tournois")
        print("3. Informations d'un Tournoi")
        print("4. Liste des joueurs d'un Tournoi")
        print("5. Détails d'un Tournoi")
        print("0. Retourner au menu principal")
        return input("\nEntrez le numéro correspondant à votre choix : ")
    