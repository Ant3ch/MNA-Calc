from menu_core import Menu, MenuItem


class MenuPrincipal(Menu):
    def __init__(self, menu_manager):
        super().__init__()
        self.menu_manager = menu_manager
        self.add_option(MenuItem("Integration numerique", self.aller_integration))
        self.add_option(MenuItem("Methode du point fixe", self.aller_point_fixe))
        self.add_option(MenuItem("Explications",          self.aller_explications))
        self.add_option(MenuItem("Credits",               self.aller_credits))

    def aller_integration(self):
        self.menu_manager.switch_menu("integration")

    def aller_point_fixe(self):
        self.menu_manager.switch_menu("point fixe")

    def aller_explications(self):
        self.menu_manager.switch_menu("explications")

    def aller_credits(self):
        self.menu_manager.switch_menu("credits")
