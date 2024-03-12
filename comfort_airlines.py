menu_options = {
    "Timetable": {
        "View": None,
        "Search routes": {
            "Sort by cost": None,
            "Sort by number of stops": None,
            "Sort by departure time": None
        },
        "Edit": {
            "Add": None,
            "Remove": None,
            "Upload": None
        },
        "Download": None,
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


def display_menu(menu):
    while True:
        print("\nMenu Options:")
        for i, key in enumerate(menu, 1):
            print(f"{i}. {key}")
        print(f"{len(menu) + 1}. Exit")
        choice = input("Enter the number of your choice: ")
        
        try:
            choice = int(choice)
            if 1 <= choice <= len(menu) + 1:
                if choice == len(menu) + 1:
                    print("Exiting program...")
                    return
                submenu_key = list(menu.keys())[choice - 1]
                submenu = menu[submenu_key]
                if submenu is None:
                    print("Selected:", submenu_key)
                else:
                    display_menu(submenu)
            else:
                print("Invalid choice. Please enter a number between 1 and", len(menu) + 1)
        except ValueError:
            print("Invalid choice. Please enter a number.")


def main():
    display_menu(menu_options)


if __name__ == "__main__":
    main()
