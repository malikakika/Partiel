import json
import os
from Models.Model import Model


class Player(Model):
    def __init__(self, first_name, last_name, birth_date, national_chess_id):
        """
        Initialise une nouvelle instance de la classe Player avec un ID unique,
        un prénom, un nom, une date de naissance
        et un ID d'échecs national.

        Args:
            first_name (str): Prénom du joueur.
            last_name (str): Nom de famille du joueur.
            birth_date (str): Date de naissance du joueur.
            national_chess_id (str): ID d'échecs national du joueur.
        """
        self.id = self.get_new_id('data/players.json')
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
        self.national_chess_id = national_chess_id

    def save_player(self):
        """
        Enregistre le joueur actuel dans le fichier players.json.
        Si le fichier n'existe pas, il sera créé.
        """
        new_player = self.__dict__
        if not os.path.exists('data/players.json'):
            with open('data/players.json', 'w') as file:
                json.dump([new_player], file, indent=4)
        else:
            with open('data/players.json', 'r+') as file:
                players = json.load(file)
                players.append(new_player)
                file.seek(0)
                file.truncate()
                json.dump(players, file, indent=4)
                 
    def get_players(self):
        """
        Charge et retourne la liste des joueurs depuis le fichier players.json.
        Si le fichier n'existe pas, renvoie un message d'erreur.

        Returns:
            list/dict/None: Liste des joueurs si le fichier existe, un message d'erreur sinon.
        """
        file_path = 'data/players.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                players = json.load(file)
                return players
        else:
            return print('Fichier players.json introuvable')
