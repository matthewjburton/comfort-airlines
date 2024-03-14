"""
Returns number of people flying from Airport A to Airport B based on metro population

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""

import airport
import flight_angle

def individual_demand(startingAirport, endingAirport):

    airport_pop = endingAirport.get_metro_population()
    flyer_percent = airport_pop/airport.total_population

    percent_flying_out = .005
    
    num_flying_out = startingAirport.get_metro_population() * percent_flying_out

    #Number of people from startingAirport who want to fly to endingAirport
    return num_flying_out * flyer_percent
        
