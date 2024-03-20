
# Purpose: Returns the time in minutes on how long it will take in minutes to travel from one airport to another depending on the aircraft model.
# Authors: Kevin Sampson, Matt Burton, McHale Trotter, Ryan Hirscher, Jeremy Maas, Justin Chen
# How to execute : python3 flight-duration.py 
# You will prompted with:  
# Enter the departure airport abbreviation : (example) JFK
# Enter the destination airport abbreviation: (example) LAX
# Enter the aircraft model: (example) 737-600
# the following information will display : Maximum Speed, Actual Speed (90% of Max), Distance, Adjustment Factor, Adjusted Speed and Estimated flight time
# additianl inforamtion is for debegging, but can be kept if pleased 

import math
from sqlalchemy import create_engine, text


# This function calculates the estimated flight time based on departure and destination airport coordinates, and aircraft model.
def calculate_flight_time(db_config):
    # Connect to the database
    engine = create_engine(f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['dbname']}")
    #Prompt the user for input:
    departure_airport = input("Enter the departure airport abbreviation: ")
    destination_airport = input("Enter the destination airport abbreviation: ")
    aircraft_model = input("Enter the aircraft model: ")
    
    # Gets aircraft max speed from the database based on the aircraft model
    with engine.connect() as conn:
        aircraft_data = conn.execute(text("SELECT maximum_speed FROM aircraft WHERE model = :model"), {"model": aircraft_model}).fetchone()
        if aircraft_data:
            maximum_speed = aircraft_data[0]
        else:
            print(f"No data found for aircraft model {aircraft_model}.")
            return
    #Gets coordinates for departure and destination airports.
        departure_coords = conn.execute(text("SELECT latitude, longitude FROM airports WHERE abbreviation = :abbr"), {"abbr": departure_airport}).fetchone()
        destination_coords = conn.execute(text("SELECT latitude, longitude FROM airports WHERE abbreviation = :abbr"), {"abbr": destination_airport}).fetchone()

    if not departure_coords or not destination_coords or not maximum_speed:
        print("Missing data for calculation.")
        return

    # Calculate the actual speed as 90% of the maximum speed
    actual_speed = maximum_speed * 0.9

    # Calculates the distance between the departure and destination airports using the haversine formula
    distance = haversine((departure_coords[0], departure_coords[1]), (destination_coords[0], destination_coords[1]))
    # Calculates the adjustment factor based on wind and bearing
    adjustment_factor = calculate_percentage(*departure_coords, *destination_coords)
    # Adjust the actual speed with wind calculation 
    adjusted_speed = actual_speed * adjustment_factor

    # Calculates the flight time in hours and convert it to minutes
    flight_time_hours = distance / adjusted_speed
    adjusted_flight_time_minutes = flight_time_hours * 60
    
    #prints information, can be useful for debugging
    print(f"Maximum Speed: {maximum_speed:.2f} mph")
    print(f"Actual Speed (90% of Max): {actual_speed:.2f} mph")
    print(f"Distance: {distance:.2f} miles")
    print(f"Adjustment Factor: {adjustment_factor:.2f}")
    print(f"Adjusted Speed: {adjusted_speed:.2f} mph")
    
    # Ask user if refueling or passenger transfer is needed
    refuel = input("Will the flight need to refuel? (yes/no): ").lower() == 'yes'
    transfer_passengers = input("Are there transferring passengers? (yes/no): ").lower() == 'yes'
    
    # Calculate the additional times based on user input
    additional_times = calculate_additional_times(refuel, transfer_passengers)
    # Adds additional times to the adjusted flight time
    total_flight_and_additional_time = adjusted_flight_time_minutes + additional_times

    # Print additional time
    print(f"Additional Time at Gate: {additional_times} minutes")
    
    #total time of flight with gate time 
    print(f"Total Flight Time including Additional Times: {total_flight_and_additional_time:.2f} minutes")
    #adjusted_flight_time_minutes = flight_time_minutes * adjustment_factor
    return adjusted_flight_time_minutes

# New function to calculate additional times at the gate
def calculate_additional_times(refuel=False, transfer_passengers=False):
    times = {
        'turnaround': 40,
        'exit_passengers': 15,
        'cleaning': 10,
        'boarding': 15,
        'refueling': 10 if refuel else 0,
        'transfer': 30 if transfer_passengers else 0,
    }
    # Returns the total of all applicable times
    return sum(times.values())  


# Calculates the distance from the coordinates
def haversine(coord1, coord2):
    R = 3958.8  # Radius of the Earth in miles
    lat1, lon1 = coord1
    lat2, lon2 = coord2
    # Convert coordinates from degrees to radians.
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    # Calculate differences in coordinates.
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Applies the haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    return distance


# Calculates the adjustment factor for flight speed based on wind ( Refrenceses Jeremys angle fucntion)
def calculate_percentage(lat1, lon1, lat2, lon2, wind=0.045):
 # Calculate the difference in longitude and handle special cases
    dif = lon2 - lon1
    if dif == 0: # Vertical flight, no wind effect.
        return 1
    if lat1 == lat2: # Horizontal flight, apply wind effect directly
        return 1 - wind if dif > 0 else 1 + wind
    
    # Calculate bearing angle and adjust speed based on wind   
    X = math.cos(math.radians(lat2)) * math.sin(math.radians(dif))
    Y = math.cos(math.radians(lat1)) * math.sin(math.radians(lat2)) - math.sin(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.cos(math.radians(dif))
    Z = math.degrees(math.atan2(X, Y))

    # Apply wind adjustment based on bearing angle
    if Z < 0:  # East to West flight, increase speed.
        Z = Z / 90
        Z = 1 + (Z * -1 * wind)
    else:  # West to East flight, potentially reduce speed
        Z = Z / 90
        Z = 1 - (Z * wind)
    return Z



# Database configuration
db_config = {
    'user': 'admin',
    'password': 'Cloud9',
    'host': 'localhost',
    'dbname': 'cloudnine'
}

# Call the function with the database configuration
flight_time = calculate_flight_time(db_config)
if flight_time is not None:
    print(f"Estimated flight time: {flight_time:.2f} minutes")

