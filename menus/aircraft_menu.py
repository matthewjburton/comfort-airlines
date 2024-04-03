"""
Class responsible for implementing the menu options under the aircraft menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter and Matt Burton
"""
from utilities.display_menu import display_menu
from utilities.database import Database

class AircraftMenu:

    """Aircraft Options"""
    @staticmethod
    def view_aircraft():
        print("\nExecuting view_aircraft()")
        # Initialize the Database object
        db = Database()

        # Show all aircraft in the database for reference
        sql = "SELECT * FROM aircraft"
        
        try:
            # Execute the select query, (returns dataframe)
            df = db.execute_query_to_dataframe(sql)
            # Print the dataframe
            print(df)
        except Exception as e:
            print(f"Error printing aircraft table: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()


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
    

