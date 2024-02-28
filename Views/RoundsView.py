class RoundsView:
    def ask_for_next_round(self):
        """
        Demande à l'utilisateur s'il souhaite passer au prochain round.

        Returns:
            str: Réponse de l'utilisateur (o pour oui, n pour non).
        """
        return input("Voulez-vous passer au round suivant ? o/n: ").strip().lower()
