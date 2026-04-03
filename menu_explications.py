from menu_core import Menu, MenuItem


class MenuExplications(Menu):
    def __init__(self, menu_manager):
        Menu.__init__(self)
        self.menu_manager = menu_manager
        self.add_option(MenuItem("Methodes integration", self.aller_integration))
        self.add_option(MenuItem("Methodes point fixe", self.aller_point_fixe))

    def aller_integration(self):
        self.menu_manager.switch_menu("explications_integration")

    def aller_point_fixe(self):
        self.menu_manager.switch_menu("explications_point_fixe")

 
class MenuExplicationsIntegration(Menu):
    
    def __init__(self):
        Menu.__init__(self)
        self.add_option(MenuItem("Riemann", self.exp_riemann))
        self.add_option(MenuItem("Trapeze", self.exp_trapeze))
        self.add_option(MenuItem("Milieu",  self.exp_milieu))
        self.add_option(MenuItem("Simpson", self.exp_simpson))
        self.add_option(MenuItem("Romberg", self.exp_romberg))
    def _affiche(self, titre, lignes):
        print("\n--- " + titre + " ---")
        i = 0
        while i < len(lignes):
            print(lignes[i])
            i += 1
        input("\n[Entree]")

    def exp_riemann(self):
        self._affiche("Riemann", [
            "Decoupe [a,b] en n",
            "Gauche : f(a+i*h)",
            "Droite : f(a+(i+1)*h)",
            "Precision O(h)"
        ])

    def exp_trapeze(self):
        self._affiche("Trapeze", [
            "Approx par trapezes",
            "(f(a)+f(b))/2",
            "+ somme interieure",
            "Precision O(h^2)"
        ])

    def exp_milieu(self):
        self._affiche("Milieu", [
            "Centre intervalle",
            "f(a+(i-0.5)*h)",
            "Precision O(h^2)"
        ])

    def exp_simpson(self):
        self._affiche("Simpson", [
            "Combine trapeze+milieu",
            "Precision O(h^4)"
        ])

    def exp_romberg(self):
        self._affiche("Romberg", [
            "Extrapolation",
            "Tres precis"
        ])

class MenuExplicationsPointFixe(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.add_option(MenuItem("Point fixe", self.exp_point_fixe))
        self.add_option(MenuItem("Newton",     self.exp_newton))
        self.add_option(MenuItem("Corde",      self.exp_corde))
        self.add_option(MenuItem("Contractante def", self.exp_contractantedef))
        self.add_option(MenuItem("Contractante critere", self.exp_contractantecritere))
        self.add_option(MenuItem("Repulsif", self.exp_repulsif))
    def _affiche(self, titre, lignes):
        print("\n--- " + titre + " ---")
        i = 0
        while i < len(lignes):
            print(lignes[i])
            i += 1
        input("\n[Entree]")
    def exp_point_fixe(self):
        self._affiche("Point fixe", [
            "x(n+1)=g(x)",
            "con:g C0,CV si |g'|<1",
            "Con:g([a,b])∈[a,b]=>CV "
        ])

    def exp_newton(self):
        self._affiche("Newton", [
            "x(n+1)=x-f/f'",
            "f C2 , x0 proche avec corde",
            "f'!=0",
            "f(a)*f(b)<0 idealement",
        ])
    def exp_corde(self):
        self._affiche("Corde", [
            "Method des cordes",
            "x_{n+1} = xn - f(xn)*(xn - x_{n-1})"
            "/(f(xn) - f(x_{n-1}))",
            "f C1, exist f(a) = 0 et f'(a) != 0",
            "idéalement f(x0)*f(x1)<0, sinon c lent "
        ])
    def exp_contractantedef(self):
        self._affiche("Contractante", [
            "|g(x)-g(y)|<=k|x-y|",
            "k<1",
            "=> unique fixe",
            "=> convergence"
        ])

    def exp_contractantecritere(self):
        self._affiche("Critere", [
            "|g'(x)|<=k<1",
            "=> contractante",
            "test simple"
        ])

    def exp_repulsif(self):
        self._affiche("Repulsif", [
            "|g'(x)|>1",
            "instable",
            "diverge"
        ])