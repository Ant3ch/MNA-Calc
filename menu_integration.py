from menu_core import Menu, MenuItem
from utils import ask_for_function_with_domain


class MenuIntegration(Menu):
    def __init__(self):
        Menu.__init__(self)
        self.add_option(MenuItem("Sommes de Riemann",       self.methodeRiemann))
        self.add_option(MenuItem("Methode trapeze",         self.methodeTrapeze))
        self.add_option(MenuItem("Point milieu",            self.methodeMilieu))
        self.add_option(MenuItem("Methode Simpson",         self.methodeSimpson))
        self.add_option(MenuItem("Methode Romberg",         self.methodeRomberg))

    def _run(self, label, compute):
        try:
            d = ask_for_function_with_domain(True)
            a = d["a"]
            b = d["b"]
            n = d["n"]
            f = d["f"]

            h = (b - a) / n
            result = compute(a, b, n, f, h)

            print("res:" + str(result))

        except ValueError as e:
            print("Erreur : " + str(e))
        except SyntaxError:
            print("Fonction invalide")

    # 🔹 RIEMANN
    def methodeRiemann(self):
        left = input("(1 G / any D): ").strip() == "1"

        if left:
            print("Riemann gauche")
        else:
            print("Riemann droite")

        def compute(a, b, n, f, h):
            s = 0
            i = 0
            while i < n:
                if left:
                    x = a + i * h
                else:
                    x = a + (i + 1) * h
                s += f(x)
                i += 1
            return s * h

        self._run("(Riemann)", compute)

    # 🔹 TRAPEZE
    def methodeTrapeze(self):
        def compute(a, b, n, f, h):
            s = (f(a) + f(b)) / 2
            i = 1
            while i < n:
                s += f(a + i * h)
                i += 1
            return s * h

        self._run("(trapeze)", compute)

    # 🔹 MILIEU
    def methodeMilieu(self):
        def compute(a, b, n, f, h):
            s = 0
            i = 1
            while i <= n:
                s += f(a + (i - 0.5) * h)
                i += 1
            return s * h

        self._run("(milieu)", compute)

    # 🔹 SIMPSON
    def methodeSimpson(self):
        def compute(a, b, n, f, h):
            s = f(a) + f(b)

            i = 1
            while i <= n:
                s += 4 * f(a + (i - 0.5) * h)
                i += 1

            i = 1
            while i < n:
                s += 2 * f(a + i * h)
                i += 1

            return s * h / 6

        self._run("(Simpson)", compute)

    # 🔹 ROMBERG
    def methodeRomberg(self):
        try:
            d = ask_for_function_with_domain(True)
            a = d["a"]
            b = d["b"]
            n = d["n"]
            f = d["f"]

            R = []
            i = 0
            while i <= n:
                R.append([0.0] * (n + 1))
                i += 1

            i = 0
            while i <= n:
                ni = 2 ** i
                h = (b - a) / ni

                s = (f(a) + f(b)) / 2
                k = 1
                while k < ni:
                    s += f(a + k * h)
                    k += 1

                R[i][0] = s * h
                i += 1

            j = 1
            while j <= n:
                i = j
                while i <= n:
                    R[i][j] = (4**j * R[i][j-1] - R[i-1][j-1]) / (4**j - 1)
                    i += 1
                j += 1

            print("\nRomberg :")
            j = 0
            while j <= n:
                print("ordre " + str(j) + " : " + str(round(R[n][j], 8)))
                j += 1

            print("Resultat : " + str(round(R[n][n], 8)))

        except ValueError as e:
            print("Erreur : " + str(e))
        except SyntaxError:
            print("Fonction invalide")