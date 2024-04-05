"""
Class responsible for implementing the menu options under the airport menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton, McHale Trotter
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
        headerDisplay = '{:<60} {:<15} {:<10} {:<10} {:<15} {:<8} {:<5}'.format('Airport Name', 'Abbreviation', 'Latitude', 'Longitude', 'Population', 'Gates', 'Hub')
        headerDisplay += '\n'
        print(headerDisplay)

    def print_airport(airport):
        airportDisplay = '{:<60} {:<15} {:<10} {:<10} {:<15,} {:<8} {:<5}'.format(airport['name'], airport['abbreviation'], airport['latitude'], airport['longitude'], airport['metro_population'], airport['total_gates'], airport['is_hub'])
        print(airportDisplay)

    @staticmethod
    def edit_airport():
        edit_options = {
            "Add": AirportMenu.add_airport,
            "Remove": AirportMenu.remove_airport,
        }
        display_menu(edit_options, is_submenu = True)
    
    
    """
    Edit Options
    add_airport: adds an airport from user input. (No input sanitization yet)
    remove_airport: prints the airport table and then allows user to remove an airport by airport_id.
    """
    @staticmethod
    def add_airport():
        # Initialize the Database object
        db = Database()

        name = input("Enter airport name: ")
        abbreviation = input("Enter airport abbreviation (3 characters): ")
        latitude = AirportMenu.get_valid_latitude()
        longitude = AirportMenu.get_valid_longitude()
        timezoneOffset = AirportMenu.get_valid_timezone_offset()
        metroPopulation = AirportMenu.get_valid_metro_population()
        isHub = AirportMenu.get_valid_is_hub()
        totalGates = AirportMenu.get_valid_total_gates(metroPopulation, isHub)

        # SQL query to insert data into the airports table
        sql = f"INSERT INTO airports (name, abbreviation, latitude, longitude, timezone_offset, metro_population, total_gates, is_hub) VALUES ('{name}', '{abbreviation}', {latitude}, {longitude}, {timezoneOffset}, {metroPopulation}, {totalGates}, {isHub})"

        try:
            # Execute the insert query
            db.execute_insert_update_delete_query(sql)
            print("Airport added successfully!")
        except Exception as e:
            print(f"Error adding airport: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()


    @staticmethod
    def remove_airport():
        print("\nExecuting remove_airport()")
        # Print the aircraft table
        AirportMenu.view_airport()

        # Initialize the Database object
        db = Database()

        # User input for aircraft to be remove based on aircraft_id
        airportID = input("Enter airport ID number to remove: ")

        # Check if the airport is associated with a flight before removing it
        try:
            sqlCheckFlights = f"SELECT * FROM flights WHERE departure_airport_id = {airportID} OR destination_airport_id = {airportID}"
            result = db.execute_query_to_dataframe(sqlCheckFlights)
        
            # If not associated we remove it.
            if result.empty:
                pass
            
            # If associated print an error and return.
            else:
                print("Cannot remove airport. It is associated with flights.")
                return
        except Exception as e:
                print(f"Error checking flights: {e}")
                return


        sql = f"DELETE FROM airports WHERE airport_id = {airportID}"

        try: 
            # Execute remove aircraft query
            db.execute_insert_update_delete_query(sql)
            print("Airport removed successfully!")
        except Exception as e:
            print(f"Error removing airport: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()

    def get_valid_latitude():
        while True:
            try:
                latitude = float(input("Enter latitude: "))
                if -90 <= latitude <= 90:
                    return latitude
                else:
                    print("Latitude must be in the range of -90 to +90 degrees.")
            except ValueError:
                print("Invalid input. Latitude must be a number.")
    
    def get_valid_longitude():
        while True:
            try:
                longitude = float(input("Enter longitude: "))
                if -180 <= longitude <= 180:
                    return longitude
                else:
                    print("Longitude must be in the range of -180 to +180 degrees.")
            except ValueError:
                print("Invalid input. Longitude must be a number.")

    def get_valid_timezone_offset():
        while True:
            try:
                offset = int(input("Enter timezone offset from UTC: "))
                if -12 <= offset <= 14:
                    return offset
                else:
                    print("Timezone offset must be in the range of -12 to +14 hours.")
            except ValueError:
                print("Invalid input. Timezone offset must be a number.")

    def get_valid_metro_population():
        while True:
            try:
                population = int(input("Enter metro population: "))
                if 0 <= population <= 1000000000:
                    return population
                else:
                    print("Metro population must be in the range of 0 to 1,000,000,000 people.")
            except ValueError:
                print("Invalid input. Metro population must be a number.")

    def get_valid_is_hub():
        while True:
            try:
                isHub = str(input("Is this airport a hub? 'yes' or 'no': "))
                if isHub.lower() == 'yes':
                    return 1
                elif isHub.lower() == 'no':
                    return 0
                else:
                    print("Is hub must be either 'yes' or 'no'.")
            except ValueError:
                print("Invalid input. Is hub must be a string.")

    def get_valid_total_gates(metroPopulation, isHub):
        maximum_gates = min(int(metroPopulation / 1000000), 11 if isHub else 5)
        while True:
            try:
                totalGates = int(input("Enter total number of gates: "))
                if 0 <= totalGates <= maximum_gates:
                    return totalGates
                else:
                    print(f"Total gates must be in the range of 0 to {maximum_gates} gates.")
            except ValueError:
                print("Invalid input. Total gates must be a number.")

