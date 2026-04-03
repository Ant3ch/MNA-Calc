from menu_core import Menu, MenuItem
from utils import ask_for_function, ask_for_number


class MenuPointFixe(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.add_option(MenuItem("Point fixe", self.methodePointFixe))
        self.add_option(MenuItem("Newton",     self.methodeNewton))
        self.add_option(MenuItem("Corde",      self.methodeCorde))

    def _ask_data(self):
        try:
            g = ask_for_function("g(x): ")
            x0 = ask_for_number("x0: ")
            tol = ask_for_number("tol: ")
            max_iter = int(ask_for_number("Max iter: "))
            return g, x0, tol, max_iter
        except ValueError as e:
            print("Erreur : " + str(e))
        except SyntaxError:
            print("Fonction invalide")
        return None

    # 🔹 POINT FIXE
    def methodePointFixe(self):
        data = self._ask_data()
        if data is None:
            return

        g, x0, tol, max_iter = data
        x = x0

        i = 0
        while i < max_iter:
            try:
                x_next = g(x)
            except:
                print("Erreur calc iter " + str(i+1))
                print("x = " + str(x))
                return

            if abs(x_next - x) < tol:
                print("CV en " + str(i+1) + " iter")
                print("x = " + str(round(x_next, 8)))
                return

            x = x_next
            i += 1

        print("Max iter atteint")
        print("x = " + str(round(x, 8)))

    # 🔹 NEWTON
    def methodeNewton(self):
        data = self._ask_data()
        if data is None:
            return

        f, x0, tol, max_iter = data
        df = ask_for_function("f'(x): ")

        x = x0
        i = 0

        while i < max_iter:
            try:
                dfx = df(x)

                # ⚠️ sécurité importante sur Casio
                if dfx == 0:
                    print("Derivee nulle !")
                    print("x = " + str(x))
                    return

                x_next = x - f(x) / dfx

            except:
                print("Erreur calc iter " + str(i+1))
                print("x = " + str(x))
                return

            if abs(x_next - x) < tol:
                print("CV en " + str(i+1) + " iter")
                print("x = " + str(round(x_next, 8)))
                return

            x = x_next
            i += 1

        print("Max iter atteint")
        print("x = " + str(round(x, 8)))
    # 🔹 CORDE (SECANTE)
    def methodeCorde(self):
            try:
                f = ask_for_function("f(x): ")
                x0 = ask_for_number("x0: ")
                x1 = ask_for_number("x1: ")
                tol = ask_for_number("tol: ")
                max_iter = int(ask_for_number("Max iter: "))
            except ValueError as e:
                print("Erreur : " + str(e))
                return
            except SyntaxError:
                print("Fonction invalide")
                return

            i = 0

            while i < max_iter:
                try:
                    f0 = f(x0)
                    f1 = f(x1)

                    # ⚠️ éviter division par 0
                    if f1 - f0 == 0:
                        print("Division par 0 !")
                        return

                    x_next = x1 - f1 * (x1 - x0) / (f1 - f0)

                except:
                    print("Erreur calc iter " + str(i+1))
                    print("x = " + str(x1))
                    return

                # condition d'arrêt
                if abs(x_next - x1) < tol:
                    print("CV en " + str(i+1) + " iter")
                    print("x = " + str(round(x_next, 8)))
                    return

                # mise à jour
                x0 = x1
                x1 = x_next
                i += 1

            print("Max iter atteint")
            print("x = " + str(round(x1, 8)))