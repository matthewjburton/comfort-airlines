"""
Class responsible for implementing the menu options under the airport menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.display_menu import display_menu
from utilities.database import Database
class AirportMenu:

    """Airport Options"""
    @staticmethod
    def view_airport():
        # Query the database for the airports table
        db = Database()
        query = 'SELECT * FROM airports'
        airports = db.execute_query_to_dataframe(query)

        if not airports.empty:
            AirportMenu.print_airports_header()

            for _, airport in airports.iterrows():
                airport['is_hub'] = int(airport['is_hub'])
                AirportMenu.print_airport(airport)

    def print_airports_header():
        headerDisplay = '{:<60} | {:<15} | {:<10} | {:<10} | {:<15} | {:<8} | {:<5}'.format('Airport Name', 'Abbreviation', 'Latitude', 'Longitude', 'Population', 'Gates', 'Hub')
        print(headerDisplay)

    def print_airport(airport):
        airportDisplay = '{:<60} | {:<15} | {:<10} | {:<10} | {:<15,} | {:<8} | {:<5}'.format(airport['name'], airport['abbreviation'], airport['latitude'], airport['longitude'], airport['metro_population'], airport['total_gates'], airport['is_hub'])
        print(airportDisplay)

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
    
