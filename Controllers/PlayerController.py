from Models.Player import Player
from Views.PlayerView import PlayerView


class PlayerController:
    def __init__(self):
        self.player = None
        self.playerView = None
        self.first_name = None
        self.last_name = None
        self.birth_date = None
        self.national_chess_id = None
    def add_player(self):
        """
        Demande les informations du joueur via la vue, crée une instance du joueur et l'enregistre.
        """
        self.playerView = PlayerView()
        self.first_name, self.last_name, self.birth_date,
        self.national_chess_id = self.playerView.get_player_info()
        self.player = Player(self.first_name, self.last_name, self.birth_date, self.national_chess_id)
        self.player.save_player()
        print("\nJoueur ajouté à la base de donnée avec succès !")
        
        