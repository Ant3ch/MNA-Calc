from menu_core import Menu, MenuManager
from menu_integration   import MenuIntegration
from menu_point_fixe    import MenuPointFixe
from menu_explications  import MenuExplications, MenuExplicationsIntegration, MenuExplicationsPointFixe
from menu_principal     import MenuPrincipal
from credit             import MenuCredits


def main():
    manager = MenuManager()
    manager.add_menu("integration",              MenuIntegration())
    manager.add_menu("point fixe",               MenuPointFixe())
    manager.add_menu("explications",             MenuExplications(manager))
    manager.add_menu("explications_integration", MenuExplicationsIntegration())
    manager.add_menu("principal",                MenuPrincipal(manager))
    manager.add_menu("explications_point_fixe", MenuExplicationsPointFixe())
    manager.add_menu("credits",                  MenuCredits())

    manager.set_start_menu("principal")

    while True:
        menu= manager.current_menu
        principal = True if menu == manager.menus.get("principal") else False
        print() if not principal else print("\n--- MNA calc ---")
        menu.display()
        parts = []

        if manager.can_go_back():
            parts.append("B:0")
        if menu.can_previous():
            parts.append("P:8")
        if menu.can_next():
            parts.append("N:9")
        
     
        parts.append("Pa:" + str(menu.current_page+1) + "/" + str(menu.total_pages()))
        # adding creator name 
        parts.append(" By Ant3ch") if principal else None


        # Safe join
        output = ""
        for i in range(len(parts)):
            if i > 0:
                output += "|"
            output += parts[i]

        print(output)


        # Asking user input
        choice = input("Choix: ").strip()
    

        # Navigation globale
        if choice == "0" and manager.can_go_back():
            manager.go_back()

        elif choice == "8":
            menu.prev_page()

        elif choice == "9":
            menu.next_page()
            # Navigation
  
        # Choix option
        elif choice.isdigit():  
            index = int(choice) - 1
            options = menu.get_page_options()

            if 0 <= index < len(options):
                options[index].execute()
            else:
                print("Choix invalide")

        else:
            print("Choix invalide")


main()