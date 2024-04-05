"""
Responsible for generating timetable(currently through RNG + a few other criteria)

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas, Ryan Hirscher, Kevin Sampson
"""

import random
import sys
sys.path.append('/Users/ryanhirscher/comfort-airlines/comfort-airlines-1')

#import utilities.great_circle as GC
from simulation.airport_objects import airports
from simulation.aircraft_objects import aircrafts

# Place an aircraft
# TO DO: Set aside a plane to Paris
def place_aircrafts():
    #Place reserve aircrafts
    aircrafts[1].currentAirport = "EWR"
    for ab in airports:
        if (airports[ab].abbreviation == "EWR"):
            airports[ab].add_aircraft_type(aircrafts[1].model)
            airports[ab].remove_gate()
        aircrafts[1].currentAirport = "EWR"
    aircrafts[2].currentAirport = "LAX"
    for ab in airports:
        if (airports[ab].abbreviation == "LAX"):
            airports[ab].add_aircraft_type(aircrafts[2].model)
            airports[ab].remove_gate()
        aircrafts[2].currentAirport = "LAX"    
    aircrafts[3].currentAirport = "DFW"
    for ab in airports:
        if (airports[ab].abbreviation == "DFW"):
            airports[ab].add_aircraft_type(aircrafts[3].model)
            airports[ab].remove_gate()
        aircrafts[3].currentAirport = "DFW"    
    aircrafts[4].currentAirport = "MDW"
    for ab in airports:
        if (airports[ab].abbreviation == "MDW"):
            airports[ab].add_aircraft_type(aircrafts[4].model)
            airports[ab].remove_gate()
        aircrafts[4].currentAirport = "MDW"
    #aircrafts[?].currentAirport = "going to paris"
    i = 5
    #Place the rest of the aircrafts at airports where a hub is filled up to 7 and the rest are placed randomly up to 4
    for i in aircrafts:
        # Abbreviations in aircrafts are initialized to aaa.
        # Generate a random starting airprot until conditions are met
        while aircrafts[i].currentAirport == "aaa":
            ChoiceAirport = airports[random.randint(1,31)]
            if ChoiceAirport.is_hub and ChoiceAirport.available_gates > 4:
                # Where airports abbreviation is the choiceAirport add to dictionary of airport
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        #print("is_hub: ", airports[ab].is_hub)
                        #print("Before removing hub gate at ", airports[ab].abbreviation, " gates before: ", airports[ab].available_gates)
                        airports[ab].remove_gate()
                        #print("After removing hub gate at ", airports[ab].abbreviation, " gates after: ", airports[ab].available_gates)
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
            elif not ChoiceAirport.is_hub and ChoiceAirport.available_gates > 1:
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        airports[ab].remove_gate()
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
    for x in aircrafts:
        print(x, ":", aircrafts[x].currentAirport, " ")
    for x in airports:
        print(x, ":", airports[x].abbreviation, " ", airports[x].available_gates, " ")

'''
def generate():
#Code to generate time table
    #Initialize
    for aircraft in aircrafts:
        TimeToHome = 0
        CurrentTime = 0
        TimeToNextLeg = 0 # Potential Time
        CurrentAirport = aircrafts.aircraft.airport
        while (TimeToHome + CurrentTime  < 1200): #20 hours of flying
            print(aircraft.airport + " => ")
            ChosenAirport = choose_random_airport(CurrentAirport) # Choose a random acceptable airport to fly to
            Home = nearest_home(CurrentAirport, aircraft[i].aircraftType)
            TimeToHome = flight_duration(CurrentAirport, Home) #Time it takes to fly home
            TimeToNextLeg += flight_duration(CurrentAirport, ChosenAirport)
            if (TimeToNextLeg + CurrentTime > 1200 or TimeToHome + TimeToNextLeg + CurrentTime > 1200):
                #fly home if next leg takes too long, so if time to home and time to next leg exceeds time in day
                CurrentTime += TimeToHome
                #Remove entry from airport dictionary
                Home.remove_aircraft_type(aircrafts[i].aircraftType)
                
            else:
                CurrentAirport = ChosenAirport
                CurrentTime += 90 # 1.5 hour buffer for delays and turn around
                CurrentTime += TimeToNextLeg
        print("Finished at " + CurrentAirport)


#Helper Function
#At the end of the day an airport must land at an acceptable starting airport
#We must have the next day start with the same type of aircraft at each airport
def nearest_home(currentAirport, aircraftType):
    ShortestDistance = 9999999
    # Iterate through all the airports and identify the shortest direct flight to an acceptable airport
    for i in airports:
        CurDistance = GC.great_circle(currentAirport, airports.i)
        if CurDistance > 150 and CurDistance < ShortestDistance:
            for aircraft_type in airports[i]._startingAircrafts:
                if aircraft_type == aircraftType:
                    ShortestDistance = CurDistance
                    ChosenHome = airports[i]
    return ChosenHome



#Helper Function
def choose_random_airport(startAirport):

    randomAirport = airports[random.randint(0,30)]
    if (GC.great_circle(startAirport, randomAirport) <= 150 or randomAirport.available_gates - randomAirport.inboundFlights <= 1):
        choose_random_airport(startAirport)
    return randomAirport

place_aircrafts
generate
'''
print("test")
place_aircrafts()
