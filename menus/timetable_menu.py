"""
Class responsible for implementing the menu options under the timetable main menu option

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
        # print("\nExecuting view_timetable()")
        Timetable.view_timetable()
    
    @staticmethod
    def search_routes():
        print("\nExecuting search_routes()")
        search_options = {
            "Sort by cost": TimetableMenu.sort_by_cost,
            "Sort by number of stops": TimetableMenu.sort_by_number_of_stops,
            "Sort by departure time": TimetableMenu.sort_by_departure_time,
        }
        display_menu(search_options, is_submenu = True)
    
    @staticmethod
    def edit_timetable():
        print("\nExecuting edit_timetable()")
        edit_options = {
            "Add": TimetableMenu.add_flight,
            "Remove": TimetableMenu.remove_flight,
            "Upload": TimetableMenu.upload_timetable,
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
    def add_flight():
        print("Executing add_flight()")
    
    @staticmethod
    def remove_flight():
        print("Executing remove_flight()")
    
    @staticmethod
    def upload_timetable():
        print("Executing upload_timetable()")