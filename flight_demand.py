#Purpose: Determine Departure and Destination demands in # of people
#         who want to fly out of/into different airports from another
#
#Authors: Cloud9: Jeremy Maas, Matt Burton, McHale Trotter, Justin Chen, Ryan Hirscher, Kevin Sampson

import airport
import flight_angle

def individual_demand(startingAirport, endingAirport):

    airport_pop = endingAirport.get_metro_population()
    flyer_percent = airport_pop/airport.total_population

    num_flying_out = startingAirport.get_metro_population() *.005

    #Number of people from StartingAirport who want to fly to endingAirport
    return num_flying_out * flyer_percent
        
