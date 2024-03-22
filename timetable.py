"""
Implements the funcitonality of the user options from the Timetable section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

import database

class Timetable:
    def view_timetable():
        # Query the database for the routes table
        db = database.Database()
        query = 'SELECT * FROM routes'
        dataframe = db.execute_query_to_dataframe(query)

        # Print the time table
        print(dataframe)
    
    def search_routes():
        db = database.Database()
        
        print("\nSearch for all routes between a departure and destination airport")
        departureAirport = input("Enter the abbreviation of the departure airport:")

        # Ensure that there is a route that departs from the departure airport
        query = f"""
                SELECT * 
                FROM routes 
                WHERE starting_airport_id = (
                    SELECT airport_id 
                    FROM airports 
                    WHERE abbreviation = '{departureAirport}'
                )
                """
        dataframe = db.execute_query_to_dataframe(query)

        if dataframe.empty:
            print(f"There are no routes that depart from {departureAirport}")
            return

        destinationAirport = input("Enter the abbreviation of the destination airport:")

        # Search for route between the destination and departure airports
        query = f"""
                SELECT * 
                FROM routes 
                WHERE starting_airport_id = (
                    SELECT airport_id 
                    FROM airports 
                    WHERE abbreviation = '{departureAirport}'
                )
                AND destination_airport_id = (
                    SELECT airport_id 
                    FROM airports 
                    WHERE abbreviation = '{destinationAirport}'
                )
                """
        dataframe = db.execute_query_to_dataframe(query)

        if dataframe.empty:
            print(f"There are no routes with the destination of {destinationAirport}")
            return
        
        # Print the results of the search
        print(dataframe)
        