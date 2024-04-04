"""
Returns number of people flying from Airport A to Airport B based on metro population

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""

from simulation.airport_objects import airports
from utilities.great_circle import great_circle

PERCENT_FLYING_OUT = 0.005

def individual_demand(startingAirport, endingAirport):

    reachablePopulation = 0

    for airport in airports:
        if (great_circle(startingAirport, airport) >= 150):
            reachablePopulation += airport.metro_population()

    airportPopulation = endingAirport.metro_population
    flyerPercent = airportPopulation / reachablePopulation
    
    numFlyingOut = startingAirport.metro_population * PERCENT_FLYING_OUT

    # Number of people from startingAirport who want to fly to endingAirport
    return numFlyingOut * flyerPercent
        
