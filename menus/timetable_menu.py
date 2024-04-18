"""
Responsible for implementing the menu options under the timetable main menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.display_menu import display_menu
from timetable.timetable import Timetable
class TimetableMenu:
    """Timetable Options"""

    @staticmethod
    def view_timetable():
        """
        Displays the timetable.
        """
        Timetable.view_timetable()
    
    @staticmethod
    def search_routes():
        """
        Executes the search routes submenu.
        """
        print("\nExecuting search_routes()")
        search_options = {
            "Sort by cost": TimetableMenu.sort_by_cost,
            "Sort by number of stops": TimetableMenu.sort_by_number_of_stops,
            "Sort by departure time": TimetableMenu.sort_by_departure_time,
        }
        display_menu(search_options, is_submenu = True)
    
    @staticmethod
    def edit_timetable():
        """
        Executes the edit timetable submenu.
        """
        print("\nExecuting edit_timetable()")
        edit_options = {
            "Add": TimetableMenu.add_flight,
            "Remove": TimetableMenu.remove_flight,
            "Upload": TimetableMenu.upload_timetable,
        }
        display_menu(edit_options, is_submenu=True)
    
    @staticmethod
    def download_timetable():
        """
        Executes the download timetable option.
        """
        print("\nExecuting download_timetable()")



    """Search Options"""
    @staticmethod
    def sort_by_cost():
        """
        Executes the sort by cost search option.
        """
        print("Executing sort_by_cost()")
    
    @staticmethod
    def sort_by_number_of_stops():
        """
        Executes the sort by number of stops search option.
        """
        print("Executing sort_by_number_of_stops()")
    
    @staticmethod
    def sort_by_departure_time():
        """
        Executes the sort by departure time search option.
        """
        print("Executing sort_by_departure_time()")

    
    
    """Edit Options"""
    @staticmethod
    def add_flight():
        """
        Executes the add flight edit option.
        """
        print("Executing add_flight()")
    
    @staticmethod
    def remove_flight():
        """
        Executes the remove flight edit option.
        """
        print("Executing remove_flight()")
    
    @staticmethod
    def upload_timetable():
        """
        Executes the upload timetable edit option.
        """
        print("Executing upload_timetable()")
