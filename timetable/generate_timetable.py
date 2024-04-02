"""
Responsible for generating timetable(currently through RNG + a few other criteria)

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas, Ryan Hirscher, Kevin Sampson
"""

import random
import utilities.great_circle as GC
import simulation.airport_objects as AO

airportList = AO.create_airports_from_database()

def generate():
#Code to generate time table

#Helper Function
def choose_random_airport(startAirport):

    randomAirport = airportList[random.randint(0,31)]
    if (GC.great_circle(startAirport, randomAirport) <= 150 or randomAirport.gatesAvailable - randomAirport.inboundFlights <= 1):
        choose_random_airport(startAirport)
    return randomAirport


#Helper Function
def return_to_base(plane):
#Checks if a plane needs to end at an airport the same type of plane started at
#Accounts for space at airport