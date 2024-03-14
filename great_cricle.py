"""
Return the distance in miles between two airports

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
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