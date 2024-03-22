"""
Class responsible for implementing the menu options under the airport menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from menu import display_menu
class AirportMenu:

    """Airport Options"""
    @staticmethod
    def view_airport():
        print("\nExecuting view_airport()")

    @staticmethod
    def edit_airport():
        print("\nExecuting edit_airport()")
        edit_options = {
            "Add": AirportMenu.add_airport,
            "Remove": AirportMenu.remove_airport,
        }
        display_menu(edit_options, is_submenu = True)
    
    
    """Edit Options"""
    @staticmethod
    def add_airport():
        print("\nExecuting add_airport()")

    @staticmethod
    def remove_airport():
        print("\nExecuting remove_airport()")
    
