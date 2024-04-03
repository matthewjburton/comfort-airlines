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
        # Initialize the Database object
        db = Database()

        while True:
            try:
                # Get input from the user
                tail_number = input("Enter tail number: ")
                if len(tail_number) > 20:
                    raise ValueError("Tail number exceeds maximum length (20 characters)")

                while True:
                    name = input("Enter name: ")
                    if len(name) > 255:
                        print("Name exceeds maximum length (255 characters)")
                    else:
                        break

                while True:
                    model = input("Enter model: ")
                    if len(model) > 255:
                        print("Model exceeds maximum length (255 characters)")
                    else:
                        break

                while True:
                    try:
                        maximum_speed = int(input("Enter maximum speed (miles per hour): "))
                        if maximum_speed < 0:
                            raise ValueError("Maximum speed must be a non-negative integer")
                        break
                    except ValueError:
                        print("Maximum speed must be an integer")

                while True:
                    try:
                        maximum_capacity = int(input("Enter maximum capacity (number of people): "))
                        if maximum_capacity < 0:
                            raise ValueError("Maximum capacity must be a non-negative integer")
                        break
                    except ValueError:
                        print("Maximum capacity must be an integer")

                while True:
                    try:
                        maximum_fuel = int(input("Enter maximum fuel (amount in gallons): "))
                        if maximum_fuel < 0:
                            raise ValueError("Maximum fuel must be a non-negative integer")
                        break
                    except ValueError:
                        print("Maximum fuel must be an integer")

                while True:
                    try:
                        cargo_volume = int(input("Enter cargo volume (volume in cubic feet): "))
                        if cargo_volume < 0:
                            raise ValueError("Cargo volume must be a non-negative integer")
                        break
                    except ValueError:
                        print("Cargo volume must be an integer")

                while True:
                    try:
                        leasing_cost = int(input("Enter leasing cost (price in USD): "))
                        if leasing_cost < 0:
                            raise ValueError("Leasing cost must be a non-negative integer")
                        break
                    except ValueError:
                        print("Leasing cost must be an integer")

                # SQL query to insert data into the aircraft table
                sql = f"INSERT INTO aircraft (tail_number, name, model, maximum_speed, maximum_capacity, maximum_fuel, cargo_volume, leasing_cost) VALUES ('{tail_number}', '{name}', '{model}', {maximum_speed}, {maximum_capacity}, {maximum_fuel}, {cargo_volume}, {leasing_cost})"

                # Execute the insert query
                db.execute_insert_update_delete_query(sql)
                print("Aircraft added successfully!")
                break  # Exit the loop if aircraft is successfully added

            except Exception as e:
                print(f"Error adding aircraft: {e}")
                print("Please try again.")

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


# Function calls for testing

# AircraftMenu.add_aircraft()
# AircraftMenu.remove_aircraft()
# AircraftMenu.view_aircraft()
    

