"""
Responsible for generating timetable(currently through RNG + a few other criteria)

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Ryan Hirscher and Jeremy Maas
"""

import random
import sys

from utilities.great_circle import great_circle
from utilities.flight_duration import calculate_total_flight_duration, calculate_flight_duration
from simulation.airport_objects import airports
from simulation.aircraft_objects import aircrafts
from utilities.turn_around_time import turn_around_time

# Place an aircraft
# TO DO: Set aside a plane to Paris
def place_aircrafts():
    #Place reserve aircrafts
    aircrafts[1].currentAirport = "EWR"
    for ab in airports:
        if (airports[ab].abbreviation == "EWR"):
            airports[ab].add_aircraft_type(aircrafts[1].model)
            airports[ab].add_aircraft(aircrafts[1])
            airports[ab].remove_gate()
        aircrafts[1].currentAirport = "EWR"
        aircrafts[1].hasHubbed = True
    aircrafts[2].currentAirport = "LAX"
    for ab in airports:
        if (airports[ab].abbreviation == "LAX"):
            airports[ab].add_aircraft_type(aircrafts[2].model)
            airports[ab].add_aircraft(aircrafts[2])
            airports[ab].remove_gate()
        aircrafts[2].currentAirport = "LAX"
        aircrafts[2].hasHubbed = True 
    aircrafts[3].currentAirport = "DFW"
    for ab in airports:
        if (airports[ab].abbreviation == "DFW"):
            airports[ab].add_aircraft_type(aircrafts[3].model)
            airports[ab].add_aircraft(aircrafts[3])
            airports[ab].remove_gate()
        aircrafts[3].currentAirport = "DFW"
        aircrafts[3].hasHubbed = True    
    aircrafts[4].currentAirport = "MDW"
    for ab in airports:
        if (airports[ab].abbreviation == "MDW"):
            airports[ab].add_aircraft_type(aircrafts[4].model)
            airports[ab].add_aircraft(aircrafts[4])
            airports[ab].remove_gate()
        aircrafts[4].currentAirport = "MDW"
        aircrafts[4].hasHubbed = True
    #aircrafts[?].currentAirport = "going to paris"
    i = 5
    #Place the rest of the aircrafts at airports where a hub is filled up to 7 and the rest are placed randomly up to 4
    for i in aircrafts:
        # Abbreviations in aircrafts are initialized to aaa.
        # Generate a random starting airprot until conditions are met
        while aircrafts[i].currentAirport == "aaa":
            ChoiceAirport = airports[random.randint(1,30)]
            if ChoiceAirport.is_hub and ChoiceAirport.available_gates >= 4:
                # Where airports abbreviation is the choiceAirport add to dictionary of airport
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        airports[ab].add_aircraft(aircrafts[i])
                        airports[ab].remove_gate()
                        #print("is_hub: ", airports[ab].is_hub)
                        #print("Before removing hub gate at ", airports[ab].abbreviation, " gates before: ", airports[ab].available_gates)
                        #print("After removing hub gate at ", airports[ab].abbreviation, " gates after: ", airports[ab].available_gates)
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
            elif not ChoiceAirport.is_hub and ChoiceAirport.available_gates >= 1:
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        airports[ab].add_aircraft(aircrafts[i])
                        airports[ab].remove_gate()
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
    for x in aircrafts:
        print(x, ":", aircrafts[x].currentAirport, " ")
    for x in airports:
        print(x, ":", airports[x].abbreviation, " ", airports[x].available_gates, " ")


def generate():

    clockTimer = 0
    while(clockTimer < 1200):#While simulation is not done

        for airport in airports:

            #Necessary booleans

            canTakeoff = False
            needsRefuel = True
            landingSoon = False
            landedAircraft = ""
            landed = False
            
            #If flight is landing soon or is landing now
 
            for arrivalTime in airport._inboundFlights:
                if (clockTimer - arrivalTime <= 10):
                    landed = False
                    landingSoon = True
                    print(f"Aircraft {airport._inboundFlights[arrivalTime].name()} landing soon at airport {airport.abbreviation()}. \n")
                elif(clockTimer == arrivalTime):
                    landed = True
                    landedAircraft = airport._inboundFlights[arrivalTime]
                else:
                    landed = False
                    landingSoon = False
            
            if(landed):
                airport.remove_gate()
                airport.lastLanding = 0
                airport.add_aircraft(landedAircraft) 
                airport.remove_inbound_flight(clockTimer)
                print(f"Aircraft {landedAircraft.name()} landed at airport {airport.abbreviation()} at minute {clockTimer}.\n")

            if(landingSoon):
                canTakeoff = False
            elif((airport.lastTakeoff == -1 and airport.lastLanding ==-1) or (airport.lastTakeoff >= 30 and airport.lastLanding ==-1) or (airport.lastTakeoff >= 30 and airport.lastLanding >=turn_around_time(needsRefuel))):
                canTakeoff = True
            else:
                canTakeoff = False

            if(canTakeoff):
                airport.lastTakeoff = 0
                chosenDestination = chooseAirport(airport, airport.currentAircraftList[0], clockTimer)#Will be same airport, next home, or best airport depending on time criteria
                chosenDestination.add_inbound_flight(clockTimer+calculate_flight_duration(airport.currentAircraftList[0], airport, chosenDestination), airport.currentAircraftList[0])
                print(f"Aircraft {airport.currentAircraftList[0].name()} taking off from airport {airport.abbreviation()} to Airport {chosenDestination.abbreviation()} at minute {clockTimer}.\n")
                airport.add_gate()
                airport.remove_aircraft(airport.currentAircraftList[0])
            if(airport.lastTakeoff != -1):
                airport.lastTakeoff +=1
            if(airport.lastLanding != 1):
                airport.lastLanding +=1

        clockTimer+=1#increment clock after each loop through airport
      

#Helper Function
#At the end of the day an airport must land at an acceptable starting airport
#We must have the next day start with the same type of aircraft at each airport
def nearest_home(currentAirport, aircraftType):
    ShortestDistance = 9999999
    ChosenHome = currentAirport #Just in case the algorithm fails
    # Iterate through all the airports and identify the shortest direct flight to an acceptable airport
    for i in airports:
        CurDistance = great_circle(currentAirport, airports[i])
        #Home must have a distance greater than 150 or itself
        #Then continue for all airports which will yield the shortest distance home
        if CurDistance == 0:
            if aircraftType in airports[i].starting_aircrafts:
                return currentAirport
        elif CurDistance > 150 and CurDistance < ShortestDistance and i != 31 and airports[i].available_gates > 0:
            if aircraftType in airports[i].starting_aircrafts:
                #print("Found a match when looking for a home: ", aircraftType, " and ", airports[i].starting_aircrafts, " at ", airports[i].abbreviation)
                ShortestDistance = CurDistance
                ChosenHome = airports[i]
    return ChosenHome

def chooseAirport(airport, aircraft, clockTimer):
    #bestAirport = airport #Set to current airport 
    #Use either csv file, or on the go calculate by iterating throuh list(will update dictionaries with values and choose based on that), but will choose airport based on profit index + satisfaction index combination
    #Checks will performed in this function to determine if it should fly to best airport, if aircraft should stay where it is, or if it should fly to most profitable home it can fly to 
    #will take into account inbound flights to airports, avail gates, etc

    randomAirport = airports[random.randint(1,30)]
    while randomAirport.abbreviation == airport.abbreviation:
        randomAirport = airports[random.randint(1,30)]
    if great_circle(airport, randomAirport) <= 150 or randomAirport.available_gates == 0:
        chooseAirport(airport, aircraft, clockTimer)
    return randomAirport

place_aircrafts()
generate()
