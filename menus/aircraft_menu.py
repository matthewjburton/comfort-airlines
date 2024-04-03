"""
Class responsible for implementing the menu options under the aircraft menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter and Matt Burton
"""
from utilities.database import Database
from utilities.display_menu import display_menu
class AircraftMenu:

    """Aircraft Options"""
    @staticmethod
    def view_aircraft():
        # Query the database for the aircraft table
        db = Database()
        query = 'SELECT * FROM aircraft'
        aircrafts = db.execute_query_to_dataframe(query)

        if not aircrafts.empty:
            AircraftMenu.print_aircrafts_header()

            for _, aircraft in aircrafts.iterrows():
                AircraftMenu.print_aircraft(aircraft)

    def print_aircrafts_header():
        headerDisplay = '{:<12} | {:<15} | {:<10} | {:<20} | {:<20} | {:<25} | {:<15} | {:<20}'.format('Tail Number', 'Aircraft Name', 'Model', 'Maximum Speed (mph)', 'Passenger Capacity', 'Fuel Capacity (gallons)', 'Cargo Volume', 'Leasing Cost (lbs)')
        print(headerDisplay)

    def print_aircraft(aircraft):
        aircraftDisplay = '{:<12} | {:<15} | {:<10} | {:<20,} | {:<20,} | {:<25,} | {:<15,} | {:<20,}'.format(aircraft['tail_number'], aircraft['name'], aircraft['model'], aircraft['maximum_speed'], aircraft['maximum_capacity'], aircraft['maximum_fuel'], aircraft['cargo_volume'], aircraft['leasing_cost'])
        print(aircraftDisplay)

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
    
