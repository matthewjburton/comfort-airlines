"""
Class responsible for implementing the menu options under the airport menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton, McHale Trotter
"""
import re
from utilities.display_menu import display_menu
from utilities.database import Database
class AirportMenu:

    """Airport Options"""
    @staticmethod
    def view_airports():
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

        name = AirportMenu.get_valid_name()
        if name == 'quit': return
        abbreviation = AirportMenu.get_valid_abbreviation()
        if abbreviation == 'quit': return
        latitude = AirportMenu.get_valid_latitude()
        if latitude == 'quit': return
        longitude = AirportMenu.get_valid_longitude()
        if longitude == 'quit': return
        timezoneOffset = AirportMenu.get_valid_timezone_offset()
        if timezoneOffset == 'quit': return
        metroPopulation = AirportMenu.get_valid_metro_population()
        if metroPopulation == 'quit': return
        isHub = AirportMenu.get_valid_is_hub()
        if isHub == 'quit': return
        totalGates = AirportMenu.get_valid_total_gates(metroPopulation, isHub)
        if totalGates == 'quit': return

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
        # Print the airport table
        AirportMenu.view_airports()
        print('')

        abbreviation = AirportMenu.get_valid_abbreviation()
        if abbreviation == 'quit':
            return

        db = Database()
        # Check if the airport is associated with a flight before removing it
        try:
            # Get the airport entity
            query = f"SELECT * FROM airports WHERE abbreviation = %s LIMIT 1"
            airport = db.execute_query_to_dataframe(query, (abbreviation,))

            if airport.empty:
                print(f"No airport found with the abbreviation {abbreviation}")
                return
            
            # Extracting airport ID and converting to regular Python integer
            airportID = int(airport['airport_id'].iloc[0])

            sqlCheckFlights = "SELECT * FROM flights WHERE departure_airport_id = %s OR destination_airport_id = %s"
            result = db.execute_query_to_dataframe(sqlCheckFlights, (airportID, airportID))
            
            if not result.empty:
                print("Cannot remove airport. Airport is used in the current timetable.")
                return

            sql = "DELETE FROM airports WHERE abbreviation = %s"
            db.execute_insert_update_delete_query(sql, (abbreviation,))
            print('Airport removed successfully!')

        except Exception as e:
            print(f"Error removing airport: {e}")
        finally:
            db.disconnect()

    def get_valid_name():
        while True:
            try:
                name = input("Enter airport name or 'q' to quit: ")

                if name.lower() == 'q':
                    return 'quit'
                
                name = str(name)
                if len(name) <= 255:
                    return name
                else:
                    print("Airport name cannot exceed 255 characters.")
            except ValueError:
                print("Airport name must be a string.")

    def get_valid_abbreviation():
        while True:
            try:
                abbreviation = input("Enter airport abbreviation or 'q' to quit: ")

                if abbreviation.lower() == 'q':
                    return 'quit'
                
                # Remove leading/trailing whitespace and convert to uppercase
                abbreviation = abbreviation.strip().upper()
                
                # Check if the abbreviation contains only letters and has a length of 3
                if re.match(r'^[A-Z]{3}$', abbreviation):
                    return abbreviation
                else:
                    print("Airport abbreviation must be exactly 3 characters long.")
            except ValueError:
                print("Airport abbreviation must be a string.")

    def get_valid_latitude():
        while True:
            try:
                latitude = input("Enter latitude or 'q' to quit: ")

                if latitude.lower() == 'q':
                    return 'quit'
                
                latitude = float(latitude)
                if -90 <= latitude <= 90:
                    return latitude
                else:
                    print("Latitude must be in the range of -90 to +90 degrees.")
            except ValueError:
                print("Invalid input. Latitude must be a number.")
    
    def get_valid_longitude():
        while True:
            try:
                longitude = input("Enter longitude or 'q' to quit: ")

                if longitude.lower() == 'q':
                    return 'quit'
                
                longitude = float(longitude)
                if -180 <= longitude <= 180:
                    return longitude
                else:
                    print("Longitude must be in the range of -180 to +180 degrees.")
            except ValueError:
                print("Invalid input. Longitude must be a number.")

    def get_valid_timezone_offset():
        while True:
            try:
                offset = input("Enter timezone offset from UTC or 'q' to quit: ")

                if offset.lower() == 'q':
                    return 'quit'
                
                offset = int(offset)
                if -12 <= offset <= 14:
                    return offset
                else:
                    print("Timezone offset must be in the range of -12 to +14 hours.")
            except ValueError:
                print("Invalid input. Timezone offset must be a number.")

    def get_valid_metro_population():
        while True:
            try:
                population = input("Enter metro population or 'q' to quit: ")

                if population.lower() == 'q':
                    return 'quit'
                
                population = population.replace(',','')
                population = int(population)
                if 0 <= population:
                    return population
                else:
                    print("Metro population must be a positive number of people.")
            except ValueError:
                print("Invalid input. Metro population must be an integer.")

    def get_valid_is_hub():
        while True:
            try:
                isHub = input("Is this airport a hub? 'yes' or 'no' or 'q' to quit: ")

                if isHub.lower() == 'q':
                    return 'quit'
                
                isHub = str(isHub).lower()
                if isHub == 'yes':
                    return 1
                elif isHub == 'no':
                    return 0
                else:
                    print("Is hub must be either 'yes' or 'no'.")
            except ValueError:
                print("Invalid input. Is hub must be a string.")

    def get_valid_total_gates(metroPopulation, isHub):
        maximumGates = min(int(metroPopulation / 1000000), 11 if isHub else 5)

        while True:
            try:
                totalGates = input("Enter total number of gates or 'q' to quit: ")

                if totalGates.lower() == 'q':
                    return 'quit'
                
                totalGates = int(totalGates)
                if 1 <= totalGates <= maximumGates:
                    return totalGates
                else:
                    print(f"Total gates must be in the range of 1 to {maximumGates} gates.")
            except ValueError:
                print("Invalid input. Total gates must be an integer.")

