"""
Class responsible for implementing the menu options under the aircraft menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter and Matt Burton
"""
from utilities.database import Database
from utilities.display_menu import display_menu
from utilities.database import Database

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
    
    
    """
    Edit Options
    add_aircraft: adds an aircraft from user input. (No input sanitization yet)
    remove_aircraft: prints the aircraft table and then allows user to remove an aircraft by aircraft_id.
    """
    @staticmethod
    def add_aircraft():
        print("\nExecuting add_aircraft()")
        # Initialize the Database object
        db = Database()

        # Get input from the user
        tail_number = input("Enter tail number: ")
        name = input("Enter name: ")
        model = input("Enter model: ")
        maximum_speed = int(input("Enter maximum speed (miles per hour): "))
        maximum_capacity = int(input("Enter maximum capacity (number of people): "))
        maximum_fuel = int(input("Enter maximum fuel (amount in gallons): "))
        cargo_volume = int(input("Enter cargo volume (volume in cubic feet): "))
        leasing_cost = int(input("Enter leasing cost (price in USD): "))

        # SQL query to insert data into the aircraft table
        sql = f"INSERT INTO aircraft (tail_number, name, model, maximum_speed, maximum_capacity, maximum_fuel, cargo_volume, leasing_cost) VALUES ('{tail_number}', '{name}', '{model}', {maximum_speed}, {maximum_capacity}, {maximum_fuel}, {cargo_volume}, {leasing_cost})"

        try:
            # Execute the insert query
            db.execute_insert_update_delete_query(sql)
            print("Aircraft added successfully!")
        except Exception as e:
            print(f"Error adding aircraft: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()

    @staticmethod
    def remove_aircraft():
        print("\nExecuting remove_aircraft()")
        # Print the aircraft table
        AircraftMenu.view_aircraft()

        # Initialize the Database object
        db = Database()

        # User input for aircraft to be remove based on aircraft_id
        aircraft_id = input("Enter aircraft ID number to remove: ")

        # Check if the aircraft is associated with a flight before removing it
        try:
            sql_check_flights = f"SELECT * FROM flights WHERE aircraft_id = {aircraft_id}"
            result = db.execute_query_to_dataframe(sql_check_flights)
        
            # If not associated we remove it.
            if result.empty:
                pass
            
            # If associated print an error and return.
            else:
                print("Cannot remove aircraft. It is associated with flights.")
                return
        except Exception as e:
                print(f"Error checking flights: {e}")
                return

        sql = f"DELETE FROM aircraft WHERE aircraft_id = {aircraft_id}"

        try: 
            # Execute remove aircraft query
            db.execute_insert_update_delete_query(sql)
            print("Aircraft removed successfully!")
        except Exception as e:
            print(f"Error removing aircraft: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()
