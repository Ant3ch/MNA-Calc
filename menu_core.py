class MenuItem:
    def __init__(self, name, func):
        self.name = name
        self.func = func

    def execute(self):
        self.func()


class Menu:
    def __init__(self, options=None, page_size=3):
        self.options = options if options else []
        self.page_size = page_size
        self.current_page = 0  # index (0-based)
        self.previous = False
        self.next = False

    def add_option(self, option):
        self.options.append(option)

    def total_pages(self):
        return (len(self.options) - 1) // self.page_size + 1

    def get_page_options(self):
        start = self.current_page * self.page_size
        end = start + self.page_size
        return self.options[start:end]

    def next_page(self):
        if self.current_page < self.total_pages() - 1:
            self.current_page += 1

    def prev_page(self):
        if self.current_page > 0:
            self.current_page -= 1

    def display(self):
        opts = self.get_page_options()
        i=0     
        for  opt in opts:
            name = opt.name
            if len(name) > 18:
                name = name[:15] + "..."
            print(str(i+1) + ". " + name)
            i += 1

        # OLD : Moved into main loop
        # # Navigation
        # if self.current_page > 0:
        #     print("8. Prec.")
        # if self.current_page < self.total_pages() - 1:
        #     print("9. Suiv.")

        # print(f"Page {self.current_page+1}/{self.total_pages()}")

    def can_previous(self):
        return self.current_page > 0

    def can_next(self):
        return self.current_page < self.total_pages() - 1


class MenuManager:
    def __init__(self):
        self.menus = {}
        self.history = []
        self.current_menu = None

    def add_menu(self, name, menu):
        self.menus[name] = menu

    def set_start_menu(self, name):
        if name in self.menus:
            self.current_menu = self.menus[name]
            self.history = [self.current_menu]

    def switch_menu(self, name):
        if name in self.menus:
            self.history.append(self.menus[name])
            self.current_menu = self.menus[name]
        else:
            print("Menu"+ str(name)+ ' not found.')

    def go_back(self):
        if len(self.history) > 1:
            self.history.pop()
            self.current_menu = self.history[-1]
        else:
            print("Déjà au menu principal.")

    def can_go_back(self):
        return len(self.history) > 1