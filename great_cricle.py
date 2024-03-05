# Purpose:  Return the distance in miles between two airports
# Author:   Matt Burton
# Notes:    The Airport class is entirely temprorary
#           There is example usage below the function

import math
import airport

def GreatCircle(airportOne, airportTwo):
    # Radius of the Earth in miles
    R = 3958.8
    
    # Convert latitude and longitude from degrees to radians
    lat1 = math.radians(airportOne.latitude)
    lon1 = math.radians(airportOne.longitude)
    lat2 = math.radians(airportTwo.latitude)
    lon2 = math.radians(airportTwo.longitude)
    
    # Haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c
    
    return distance

# Example usage
print("Distance between JFK and LAX: {:.3f} miles".format(GreatCircle(airport.Airport.JFK, airport.Airport.LAX)))
print("Distance between JFK and ORD: {:.3f} miles".format(GreatCircle(airport.Airport.JFK, airport.Airport.ORD)))
print("Distance between JFK and DFW: {:.3f} miles".format(GreatCircle(airport.Airport.JFK, airport.Airport.DFW)))
