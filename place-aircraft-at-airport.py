# Purpose:  Place aircraft at airports. Each airport gets at least one aircraft.
#        *  Aircraft will be placed from 0 to n-1 (airport) looping until no more aircraft are present.
#        *  Airports are sorted by metro_population (desc) so that high metros get more aircraft than low metros.
#
# Author:   McHale Trotter
#
# Date:     2/7/2024
#
# Notes:    Currently there are no aircraft in the database. This function does not actually link
#           aircraft and airports yet, (instead just prints which airports are linked).
#
# Improvements: 
#        *  Further calculation and optimization could allow planes to be distributed more densely for extremely high metros.
#-----------------------------------------------------------------------------------------------------------------------------------#


import mysql.connector

# Function to handle the process of assigning aircraft to airports.
def place_aircraft_at_airports():
    # Connect to the database
    db_connection = mysql.connector.connect(
        host="localhost",
        user="admin",
        password="Cloud9",
        database="cloudnine"
    )

    # Create a cursor object to execute SQL queries
    cursor = db_connection.cursor()

    try:
        # Retrieve information about aircraft
        cursor.execute("SELECT aircraft_id, name FROM aircraft")
        aircraft_data = cursor.fetchall()

        # Retrieve information about airports in descending order of metro_population
        cursor.execute("SELECT airport_id, name, metro_population FROM airports ORDER BY metro_population DESC")
        airport_data = cursor.fetchall()

        # Assign aircraft to airports, (until no aircraft remain)
        while aircraft_data:
            for airport in airport_data:
                if aircraft_data:
                    # Tuple unpacking to extract id and name from 'airport'
                    airport_id, airport_name, _ = airport
                    # Remove the first aircraft in 'aircraft_data'. Also send the popped aircraft into 'assigned_aircraft'. 
                    assigned_aircraft = aircraft_data.pop(0)
                    # Tuple unpacking to extract id and name from 'assigned_aircraft'
                    aircraft_id, aircraft_name = assigned_aircraft
                    # Assign the aircraft to the airport
                    # NOTE HERE: SQL query should happen here to link aircraft with airport. (I think we need a new table for this)
                    print(f"Assigned {aircraft_name} to {airport_name}")
                else:
                    break # Break out of the for loop if no more aircraft are available
                    
    except mysql.connector.Error as error:
        print("Error querying database:", error)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db_connection.close()

# Call the function to place aircraft at airports
place_aircraft_at_airports()