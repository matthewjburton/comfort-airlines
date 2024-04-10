"""
Responsible for generating timetable(currently through RNG + a few other criteria)

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Ryan Hirscher and Jeremy Maas
"""

import random
import sys
sys.path.append('/Users/ryanhirscher/comfort-airlines/comfort-airlines-1')

from utilities.great_circle import great_circle
from utilities.flight_duration import calculate_total_flight_duration
from utilities.turn_around_time import turn_around_time
from simulation.airport_objects import airports
from simulation.aircraft_objects import aircrafts

WAITBUFFER = 45

# Place an aircraft
# TO DO: Set aside a plane to Paris
def place_aircrafts():
    #Place reserve aircrafts
    aircrafts[1].currentAirport = "EWR"
    for ab in airports:
        if (airports[ab].abbreviation == "EWR"):
            airports[ab].add_aircraft_type(aircrafts[1].model)
            #airports[ab].remove_gate()
            airports[ab].reserve_gate(0,0)
            aircrafts[1].addHistory(airports[ab])
        aircrafts[1].currentAirport = "EWR"
        aircrafts[1].hasHubbed = True
    aircrafts[2].currentAirport = "LAX"
    for ab in airports:
        if (airports[ab].abbreviation == "LAX"):
            airports[ab].add_aircraft_type(aircrafts[2].model)
            #airports[ab].remove_gate()
            airports[ab].reserve_gate(0,0)
            aircrafts[2].addHistory(airports[ab])
        aircrafts[2].currentAirport = "LAX"
        aircrafts[2].hasHubbed = True 
    aircrafts[3].currentAirport = "DFW"
    for ab in airports:
        if (airports[ab].abbreviation == "DFW"):
            airports[ab].add_aircraft_type(aircrafts[3].model)
            #airports[ab].remove_gate()
            airports[ab].reserve_gate(0,0)
            aircrafts[3].addHistory(airports[ab])
        aircrafts[3].currentAirport = "DFW"
        aircrafts[3].hasHubbed = True    
    aircrafts[4].currentAirport = "MDW"
    for ab in airports:
        if (airports[ab].abbreviation == "MDW"):
            airports[ab].add_aircraft_type(aircrafts[4].model)
            #airports[ab].remove_gate()
            airports[ab].reserve_gate(0,0)
            aircrafts[4].addHistory(airports[ab])
        aircrafts[4].currentAirport = "MDW"
        aircrafts[4].hasHubbed = True
    #aircrafts[?].currentAirport = "going to paris"
    i = 5
    #Place the rest of the aircrafts at airports where a hub is filled up to 7 and the rest are placed randomly up to 4
    for i in aircrafts:
        #print("PLACING AIRCRAFT ", i)
        # Abbreviations in aircrafts are initialized to aaa.
        # Generate a random starting airprot until conditions are met
        while aircrafts[i].currentAirport == "aaa":
            ChoiceAirport = airports[random.randint(1,30)]
            if ChoiceAirport.is_hub and ChoiceAirport.available_gates >= 4:
                # Where airports abbreviation is the choiceAirport add to dictionary of airport
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        #airports[ab].remove_gate()
                        airports[ab].reserve_gate(0,0)
                        aircrafts[i].addHistory(airports[ab])
                        #print("is_hub: ", airports[ab].is_hub)
                        #print("Before removing hub gate at ", airports[ab].abbreviation, " gates before: ", airports[ab].available_gates)
                        #print("After removing hub gate at ", airports[ab].abbreviation, " gates after: ", airports[ab].available_gates)
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
            elif not ChoiceAirport.is_hub and ChoiceAirport.available_gates >= 1:
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        #airports[ab].remove_gate()
                        airports[ab].reserve_gate(0,0)
                        aircrafts[i].addHistory(airports[ab])
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
    for x in aircrafts:
        print(x, ":", aircrafts[x].currentAirport, " ")
    for x in airports:
        print(x, ":", airports[x].abbreviation, " ", airports[x].available_gates, " ")


def generate():
#Code to generate time table
    #Initialize
    for i in aircrafts:
        print("\n", aircrafts[i].tailNumber, "starting")
        isHome = False
        Staying = False
        TimeToHome = 0
        CurrentTime = 0
        TimeToNextLeg = 0 # Potential Time
        HubLeg = random.randint(0,2)
        LegNumber = 0
        for ab in airports:
            if airports[ab].abbreviation == aircrafts[i].currentAirport:
                CurrentAirport = airports[ab]
        while not isHome and TimeToNextLeg + CurrentTime  < 1000: #20 hours of flying
            for ab in airports:
                if airports[ab].abbreviation == aircrafts[i].currentAirport:
                    hab = airports[ab].is_hub
            print(aircrafts[i].currentAirport, hab, " => ", end='')
            ChosenAirport = choose_random_airport(CurrentAirport, HubLeg, LegNumber, aircrafts[i], CurrentTime) # Choose a random acceptable airport to fly to
            Home = nearest_home(CurrentAirport, aircrafts[i].model)
            NextHome = nearest_home(ChosenAirport, aircrafts[i].model)

            #Get time to home and time to next leg and compare
            TimeToHome = calculate_total_flight_duration(aircrafts[i], ChosenAirport, Home, True) #Time it takes to fly home
            TimeToNextLeg = calculate_total_flight_duration(aircrafts[i], CurrentAirport, ChosenAirport, True)
            TimeToNextHome = calculate_total_flight_duration(aircrafts[i], ChosenAirport, NextHome, True)
            if TimeToNextHome + TimeToNextLeg + CurrentTime > 1000 or TimeToNextLeg + CurrentTime > 1000 or TimeToNextHome + CurrentTime > 1000:
                #fly home if next leg and next home time exceeds current time or if the time to the next leg + current time exceeds 1200
                #take off
                print("CHECKING: ", CurrentAirport.abbreviation, Home.abbreviation)
                if CurrentAirport.abbreviation == Home.abbreviation: #Is it actually flying to home or can it stay
                    Staying = True
                #for ab in airports:
                #    if airports[ab].abbreviation == aircrafts[i].currentAirport:
                        #if not Staying:
                            #airports[ab].add_gate()
                
                CurrentTime += TimeToHome
                isHome = True
                CurrentAirport = Home
                LegNumber+=1
                aircrafts[i].currentAirport = CurrentAirport.abbreviation
                #arrive
                for ab in airports:
                    if airports[ab].abbreviation == aircrafts[i].currentAirport:
                        airports[ab].remove_aircraft_type(aircrafts[i].model)
                        #if not Staying:
                            #airports[ab].remove_gate()
                        if airports[ab].is_hub:
                            aircrafts[i].hasHubbed = True
                
            else: #take off to next leg
                #update timeToHome
                TimeToHome = TimeToNextHome
                for ab in airports:
                    if airports[ab].abbreviation == CurrentAirport.abbreviation:
                        airports[ab].reserve_gate(CurrentTime + TimeToNextLeg, CurrentTime + TimeToNextLeg + turn_around_time(True) + WAITBUFFER)
                        #airports[ab].add_gate()
                    
                aircrafts[i].addHistory(CurrentAirport.abbreviation)
                aircrafts[i].currentAirport = ChosenAirport.abbreviation
                CurrentAirport = ChosenAirport
                LegNumber+=1
                CurrentTime += turn_around_time(True) + WAITBUFFER
                CurrentTime += TimeToNextLeg
                #arrive at next leg
                for ab in airports:
                    if airports[ab].abbreviation == CurrentAirport.abbreviation and airports[ab].is_hub:
                        aircrafts[i].hasHubbed = True
        if (CurrentTime <= 1200):
            print("Finished at ", CurrentAirport.abbreviation, " at ", CurrentTime)
        else:
            rest = True
            #print("LATE RESTARTING")
            #generate()
            print("Finished at ", CurrentAirport.abbreviation, " at ", CurrentTime, " LANDING LATE!!!")

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

#Helper Function
def choose_random_airport(startAirport, HubLeg, CountToHub, aircraft, CurrentTime):
    if HubLeg == CountToHub and not aircraft.hasHubbed:
        Hubs = [2, 4, 6, 7] #Numbers of hubs
        #while (airports[HubNum].is_gate_available()):
        HubNum = random.choice(Hubs)
        return airports[HubNum]
    #airport must not be itself, or in flight path history
    #airport must not be a hub - Have at most one aicraft fly through one hub? Or should we change this?
    #airport must have an available gate when it LANDS!! (not implemented yet)
    #airport must be greater than 150 miles
    randomAirport = airports[random.randint(1,30)]
    arrivalTimeAtNew = calculate_total_flight_duration(aircraft, startAirport, randomAirport, True) + CurrentTime #Time it arrives at new airport
    departureTimeAtNew = arrivalTimeAtNew + turn_around_time(True) + WAITBUFFER #Time it leaves from new airport
    while (randomAirport.abbreviation == startAirport.abbreviation or randomAirport.is_hub or randomAirport.available_gates == 0 or aircraft.isInHistory(randomAirport.abbreviation) or great_circle(startAirport, randomAirport) <= 150) and not randomAirport.is_gate_available(arrivalTimeAtNew, departureTimeAtNew):
        randomAirport = airports[random.randint(1,30)]
        arrivalTimeAtNew = calculate_total_flight_duration(aircraft, startAirport, randomAirport, True) + CurrentTime #Time it arrives at new airport
        departureTimeAtNew = arrivalTimeAtNew +  turn_around_time(True) + WAITBUFFER #Time it leaves from new airport
    return randomAirport

place_aircrafts()
generate()
