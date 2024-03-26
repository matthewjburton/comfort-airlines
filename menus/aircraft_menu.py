"""
Class responsible for implementing the menu options under the aircraft menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter and Matt Burton
"""
from utilities.display_menu import display_menu
class AircraftMenu:

    """Aircraft Options"""
    @staticmethod
    def view_aircraft():
        print("\nExecuting view_aircraft()")

    @staticmethod
    def edit_aircraft():
        print("\nExecuting edit_aircraft()")
        edit_options = {
            "Add": AircraftMenu.add_aircraft,
            "Remove": AircraftMenu.remove_aircraft,
        }
        display_menu(edit_options, is_submenu = True)
    
    
    """Edit Options"""
    @staticmethod
    def add_aircraft():
        print("\nExecuting add_aircraft()")

    @staticmethod
    def remove_aircraft():
        print("\nExecuting remove_aircraft()")
    

