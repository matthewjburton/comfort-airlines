"""
The main executable program for the user interface. 
Responsible for displaying the features and options menus and calling the corresponding methods.

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from timetable import Timetable

menu_options = {
    "Timetable": {
        "View": Timetable.view_timetable,
        "Search routes": Timetable.search_routes,
        "Edit": Timetable.edit_timetable,
        "Download": Timetable.download_timetable,
    },
    "Simulation": {
        "Run": None,
        "Configure": {
            "Start date": None,
            "Duration": None,
            "Report frequency": None,
            "Costs": {
                "Fuel": None,
                "Gate": None,
                "Takeoff": None,
                "Landing": None,
                "Aircraft": None
            },
            "Challenges": {
                "View": None,
                "Edit": None
            }
        },
        "Analyze": {
            "Follow aircraft": None,
            "Download report(s)": None
        },
    },
    "Airports": {
        "View": None,
        "Edit": {
            "Add": None,
            "Remove": None
        },
    },
    "Aircraft": {
        "View": None,
        "Edit": {
            "Add": None,
            "Remove": None
        },
    },
}

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

def main():
    display_menu(menu_options)

if __name__ == "__main__":
    main()
