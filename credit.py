from menu_core import Menu, MenuItem


class MenuCredits(Menu):
    def __init__(self):
        super().__init__()
        self.add_option(MenuItem("Afficher les credits", self.show_credits))
        self.add_option(MenuItem("Afficher le GitHub", self.show_github))

    def show_credits(self):
        self._affiche("Credits", [
            "Projet : MNA Calculator",
            "Auteur : Ducourtioux",
            "Version : 1.0",
            "",
            "Outil pedagogique d'analyse numerique",
            "Integration numerique, point fixe, Newton, corde",
            "",
            "Developpe pour Python / calculatrice Casio",
            "2026",
        ])

    def show_github(self):
        self._affiche("GitHub", [
            "https://github.com/Ant3ch",
        ])

    def _affiche(self, titre, lignes):
        print("\n--- " + titre + " ---")
        i = 0
        while i < len(lignes):
            print(lignes[i])
            i += 1
        input("\n[Entree]")