import re


class View:

    def is_valid_date(self, date):
        """
        Vérifie si la chaîne de caractères fournie est une date valide au format JJ/MM/AAAA.

        Args:
            date (str): Chaîne de caractères à vérifier.

        Returns:
            bool: True si la date est valide, sinon False.
        """
        return re.fullmatch(r'\d{2}/\d{2}/\d{4}', date) is not None

    def is_valid_id(self, id):
        """
        Vérifie si la chaîne de caractères fournie est un ID valide.

        Args:
            id (str): Chaîne de caractères à vérifier.

        Returns:
            bool: True si l'ID est valide, sinon False.
        """
        return re.fullmatch(r'[A-Za-z]{2}\d{5}', id) is not None

    def is_valid_alpha(self, input_string):
        """
        Vérifie si la chaîne de caractères fournie contient uniquement
        des caractères alphabétiques (et des espaces).

        Args:
            input_string (str): Chaîne de caractères à vérifier.

        Returns:
            bool: True si la chaîne est valide, sinon False.
        """
        return re.fullmatch(r'[A-Za-zÀ-ÖØ-öø-ÿ\s]{2,}', input_string) is not None

    def is_valid_int(self, input_string):
        """
        Vérifie si la chaîne de caractères fournie représente un entier valide.

        Args:
            input_string (str): Chaîne de caractères à vérifier.

        Returns:
            bool: True si la chaîne représente un entier valide, sinon False.
        """
        return input_string.isdigit()

    def get_valid_date_input(self, prompt):
        """
        Demande à l'utilisateur d'entrer une date au format JJ/MM/AAAA
        jusqu'à ce qu'une entrée valide soit fournie.

        Args:
            prompt (str): L'invite affichée à l'utilisateur.

        Returns:
            str: Date valide entrée par l'utilisateur.
        """
        while True:
            date = input(prompt)
            if self.is_valid_date(date):
                return date
            else:
                print("Date invalide. Réessayez.")

    def get_valid_alpha_input(self, prompt):
        """
        Demande à l'utilisateur d'entrer une chaîne alphabétique jusqu'à ce
        qu'une entrée valide soit fournie.

        Args:
            prompt (str): L'invite affichée à l'utilisateur.

        Returns:
            str: Chaîne alphabétique valide entrée par l'utilisateur.
        """
        while True:
            input_string = input(prompt)
            if self.is_valid_alpha(input_string):
                return input_string
            else:
                print("Entrée invalide. Réessayez avec au moins deux caractères alphabétiques.")

    def get_valid_int_input(self, prompt, default_value=None):
        """
        Demande à l'utilisateur d'entrer un entier jusqu'à ce qu'une entrée valide soit fournie.
        Si l'utilisateur n'entre rien et qu'une valeur par défaut est fournie,
        renvoie cette valeur par défaut.

        Args:
            prompt (str): L'invite affichée à l'utilisateur.
            default_value (int, optional): Valeur par défaut à retourner si l'utilisateur n'entre rien.

        Returns:
            int: Entier valide entré par l'utilisateur ou valeur par défaut si fournie.
        """
        while True:
            input_string = input(prompt)
            if input_string == "" and default_value is not None:
                return default_value
            elif input_string.isdigit():
                return int(input_string)
            else:
                print("Entrée invalide, veuillez entrer un caractère numérique.")
