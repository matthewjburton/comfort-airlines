"""
Return the distance in miles between two airports

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
import math

RADIUS = 3958.8 # Radius of the Earth in miles

def great_circle(airportOne, airportTwo):
    # Convert latitude and longitude from degrees to radians
    latitudeOne = math.radians(airportOne.latitude)
    longitudeOne = math.radians(airportOne.longitude)
    latitudeTwo = math.radians(airportTwo.latitude)
    longitudeTwo = math.radians(airportTwo.longitude)
    
    # Calculate coordinate deltas
    deltaLatitude = latitudeTwo - latitudeOne
    deltaLongitude = longitudeTwo - longitudeOne

    # Intermediate calculations for Haversine formula
    intermediateTerm = math.sin(deltaLatitude / 2)**2 + math.cos(latitudeOne) * math.cos(latitudeTwo) * math.sin(deltaLongitude / 2)**2
    haversineTerm = 2 * math.atan2(math.sqrt(intermediateTerm), math.sqrt(1 - intermediateTerm))

    # Final distance calculation
    distance = RADIUS * haversineTerm
    
    return distance