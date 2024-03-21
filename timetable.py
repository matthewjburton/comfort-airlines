"""
Class responsible for implementing the menu options under the timetable main menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
class Timetable:

    """Timetable Options"""
    @staticmethod
    def view_timetable():
        print("\nExecuting view_timetable()")
    
    @staticmethod
    def search_routes():
        print("\nExecuting search_routes()")
        search_options = {
            "Sort by cost": Timetable.sort_by_cost,
            "Sort by number of stops": Timetable.sort_by_number_of_stops,
            "Sort by departure time": Timetable.sort_by_departure_time,
        }
        display_menu(search_options, is_submenu=True)
    
    @staticmethod
    def edit_timetable():
        print("\nExecuting edit_timetable()")
        edit_options = {
            "Add": Timetable.add_route,
            "Remove": Timetable.remove_route,
            "Upload": Timetable.upload_timetable,
        }
        display_menu(edit_options, is_submenu=True)
    
    @staticmethod
    def download_timetable():
        print("\nExecuting download_timetable()")


    """Search Options"""
    @staticmethod
    def sort_by_cost():
        print("Executing sort_by_cost()")
    
    @staticmethod
    def sort_by_number_of_stops():
        print("Executing sort_by_number_of_stops()")
    
    @staticmethod
    def sort_by_departure_time():
        print("Executing sort_by_departure_time()")

    
    """Edit Options"""
    @staticmethod
    def add_route():
        print("Executing add_route()")
    
    @staticmethod
    def remove_route():
        print("Executing remove_route()")
    
    @staticmethod
    def upload_timetable():
        print("Executing upload_timetable()")

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
                        print("Going back")
                        return
                    else:
                        print("Exiting program")
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