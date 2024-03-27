"""
Displays lists of options and handles user input for selecting an option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
def display_menu(menu, is_submenu=False):
    while True:
        print("\nMenu Options:")
        for i, key in enumerate(menu, 1):
            print(f"{i}. {key}")
        if is_submenu:
            print(f"{len(menu) + 1}. Back")
        else:
            print(f"{len(menu) + 1}. Exit")
        choice = input("Enter the number of your choice: ")
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(menu) + 1:
                if choice == len(menu) + 1:
                    if is_submenu:
                        print("Going back...")
                        return
                    else:
                        print("Exiting program...")
                        return
                submenu_key = list(menu.keys())[choice - 1]
                submenu = menu[submenu_key]
                if callable(submenu):  # Check if the submenu is a function
                    submenu()  # Execute the function
                elif submenu is not None:
                    display_menu(submenu, is_submenu=True)
            else:
                print("Invalid choice. Please enter a number between 1 and", len(menu) + 1)
        except ValueError:
            print("Invalid choice. Please enter a number.")