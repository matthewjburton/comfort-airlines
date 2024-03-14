"""
Returns number of people flying from Airport A to Airport B based on metro population

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""

import airport

def individual_demand(startingAirport, endingAirport):

    airportPopulation = endingAirport.get_metro_population()
    flyerPercent = airportPopulation/airport.total_population

    PERCENT_FLYING_OUT = 0.005
    
    numFlyingOut = startingAirport.get_metro_population() * PERCENT_FLYING_OUT

    #Number of people from startingAirport who want to fly to endingAirport
    return numFlyingOut * flyerPercent
        
