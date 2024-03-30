"""
Class responsible for implementing the menu options under the airport menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton, McHale Trotter
"""
<<<<<<< HEAD:menus/airport_menu.py
from utilities.display_menu import display_menu
=======
from menu import display_menu
import database
>>>>>>> 0223c7e (Added add_airport(), view_airport(),):airport_menu.py
class AirportMenu:

    """Airport Options"""
    @staticmethod
    def view_airport():
        print("\nExecuting view_airport()")
        # Initialize the Database object
        db = database.Database()

        # Show all aircraft in the database for reference
        sql = "SELECT * FROM airports"
        
        try:
            # Execute the select query, (returns dataframe)
            df = db.execute_query_to_dataframe(sql)

            # Adjust the 'is_hub' attribute to be interpolated as an int
            df['is_hub'] = df['is_hub'].astype(int)

            # Print the dataframe
            print(df)
        except Exception as e:
            print(f"Error printing airports table: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()

    @staticmethod
    def edit_airport():
        print("\nExecuting edit_airport()")
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
        print("\nExecuting add_airport()")
        # Initialize the Database object
        db = database.Database()

        name = input("Enter airport name: ")
        abbreviation = input("Enter airport abbreviation (3 characters): ")
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
        timezone_offset = int(input("Enter timezone offset (hours from UTC): "))
        metro_population = int(input("Enter metro population: "))
        total_gates = int(input("Enter total number of gates: "))
        is_hub = int(input("Is this airport a hub? (1 for yes, 0 for no): "))

        # SQL query to insert data into the airports table
        sql = f"INSERT INTO airports (name, abbreviation, latitude, longitude, timezone_offset, metro_population, total_gates, is_hub) VALUES ('{name}', '{abbreviation}', {latitude}, {longitude}, {timezone_offset}, {metro_population}, {total_gates}, {is_hub})"

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
        db = database.Database()

        # User input for aircraft to be remove based on aircraft_id
        airport_id = input("Enter airport ID number to remove: ")

        # Check if the airport is associated with a flight before removing it
        try:
            sql_check_flights = f"SELECT * FROM flights WHERE departure_airport_id = {airport_id} OR destination_airport_id = {airport_id}"
            result = db.execute_query_to_dataframe(sql_check_flights)
        
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


        sql = f"DELETE FROM airports WHERE airport_id = {airport_id}"

        try: 
            # Execute remove aircraft query
            db.execute_insert_update_delete_query(sql)
            print("Airport removed successfully!")
        except Exception as e:
            print(f"Error removing airport: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()


# Function calls for testing

# AirportMenu.view_airport()
# AirportMenu.add_airport()
# AirportMenu.remove_airport()
