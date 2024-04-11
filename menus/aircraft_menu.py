"""
Class responsible for implementing the menu options under the aircraft menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter and Matt Burton
"""
import re
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
        # Initialize the Database object
        db = Database()

        tailNumber = AircraftMenu.get_valid_tail_number()
        if tailNumber == 'quit': return

        name = AircraftMenu.get_valid_name_or_model("name")
        if name == 'quit': return

        model = AircraftMenu.get_valid_name_or_model("model")
        if model == 'quit': return

        maximumSpeed = AircraftMenu.get_int_value("maximum speed (MPH)")
        if maximumSpeed == 'quit': return

        maximumCapacity = AircraftMenu.get_int_value("maximum capacity (number of people)")
        if maximumCapacity == 'quit': return

        maximumFuel = AircraftMenu.get_int_value("maximum fuel (gallons)")
        if maximumFuel == 'quit': return

        cargoVolume = AircraftMenu.get_int_value("cargo volume (cubic feet)")
        if cargoVolume == 'quit': return

        leasingCost = AircraftMenu.get_int_value("leasing cost (USD)")
        if leasingCost == 'quit': return

        # SQL query to insert data into the aircraft table
        sql = "INSERT INTO aircraft (tail_number, name, model, maximum_speed, maximum_capacity, maximum_fuel, cargo_volume, leasing_cost) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        values = (tailNumber, name, model, maximumSpeed, maximumCapacity, maximumFuel, cargoVolume, leasingCost)
        
        try:
            # Execute the insert query
            db.execute_insert_update_delete_query(sql, values)
            print("Aircraft added successfully!")
        except Exception as e:
            print(f"Error adding aircraft: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()

    @staticmethod
    def remove_aircraft():
        # Print the aircraft table
        AircraftMenu.view_aircraft()

        # Initialize the Database object
        db = Database()

        # User input for aircraft to be remove based on aircraft_id
        tailNum = input("Enter aircraft tail number to remove or 'q' to quit: ")
        if tailNum == 'q':
            return

        sql_check_aircraft = f"SELECT aircraft_id FROM aircraft WHERE tail_number = {tailNum}"
        aircraftID_df = db.execute_query_to_dataframe(sql_check_aircraft)

        # Check if the aircraft exists in the database
        if aircraftID_df.empty:
            print("Aircraft not found.")
            return
        
        # Extract the aircraft ID from the DataFrame
        aircraftID = aircraftID_df.iloc[0]['aircraft_id']
        
        # Check if the aircraft is associated with a flight before removing it
        try:
            sql_check_flights = f"SELECT * FROM flights WHERE aircraft_id = {aircraftID}"
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

        sql = f"DELETE FROM aircraft WHERE aircraft_id = {aircraftID}"

        try: 
            # Execute remove aircraft query
            db.execute_insert_update_delete_query(sql)
            print("Aircraft removed successfully!")
        except Exception as e:
            print(f"Error removing aircraft: {e}")
        finally:
            # Disconnect from the database
            db.disconnect()

    def get_valid_tail_number():
        db = Database()
        query = 'SELECT * FROM aircraft'
        aircraft = db.execute_query_to_dataframe(query)

        while True:
            try:
                # Get input from the user
                tailNumber = input("Enter tail number or 'q' to quit: ")
            
                if tailNumber.lower() == 'q':
                    return 'quit'
                
                tailNumber = str(tailNumber)

                if tailNumber in aircraft['tail_number'].values:
                    print("Aircraft tail number already exists. Please enter a different tail number.")
                    continue
                
                if len(tailNumber) <= 20:
                    return tailNumber
                else:
                    print("Aircraft tail number cannot exceed 20 characters.")
            except ValueError:
                print("Tail number must be a string.")


    def get_valid_name_or_model(input_type):
        while True:
                try:
                    user_input = input(f"Enter aircraft {input_type} or 'q' to quit: ")

                    if user_input.lower() == 'q':
                        return 'quit'

                    if len(user_input) <= 255:
                        return user_input
                    else:
                        print(f"Aircraft {input_type} cannot exceed 255 characters.")
                except ValueError:
                    print(f"Aircraft {input_type} must be a string.")

    def get_int_value(input_type):
        while True:
            try:
                user_input = input(f"Enter {input_type} or 'q' to quit: ")

                if user_input.lower() == 'q':
                    return 'quit'
                
                user_input = int(user_input)

                if user_input >= 0:
                    return user_input
                else:
                    print(f"Aircraft {input_type} must be a non-negative integer.")
            except ValueError:
                print(f"Aircraft {input_type} must be an integer.")