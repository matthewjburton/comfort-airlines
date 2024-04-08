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
        aircrafts[1].hasHubbed = True
    aircrafts[2].currentAirport = "LAX"
    for ab in airports:
        if (airports[ab].abbreviation == "LAX"):
            airports[ab].add_aircraft_type(aircrafts[2].model)
            airports[ab].remove_gate()
        aircrafts[2].currentAirport = "LAX"
        aircrafts[2].hasHubbed = True 
    aircrafts[3].currentAirport = "DFW"
    for ab in airports:
        if (airports[ab].abbreviation == "DFW"):
            airports[ab].add_aircraft_type(aircrafts[3].model)
            airports[ab].remove_gate()
        aircrafts[3].currentAirport = "DFW"
        aircrafts[3].hasHubbed = True    
    aircrafts[4].currentAirport = "MDW"
    for ab in airports:
        if (airports[ab].abbreviation == "MDW"):
            airports[ab].add_aircraft_type(aircrafts[4].model)
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
            if ChoiceAirport.is_hub and ChoiceAirport.available_gates > 4:
                # Where airports abbreviation is the choiceAirport add to dictionary of airport
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model)
                        airports[ab].remove_gate()
                        #print("is_hub: ", airports[ab].is_hub)
                        #print("Before removing hub gate at ", airports[ab].abbreviation, " gates before: ", airports[ab].available_gates)
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


def generate():
#Code to generate time table
    #Initialize
    for i in aircrafts:
        print("\n", aircrafts[i].tailNumber, "starting")
        isHome = False
        TimeToHome = 0
        CurrentTime = 0
        TimeToNextLeg = 0 # Potential Time
        HubLeg = random.randint(0,3)
        LegNumber = 0
        for ab in airports:
            if airports[ab].abbreviation == aircrafts[i].currentAirport:
                CurrentAirport = airports[ab]
        while not isHome and TimeToHome + CurrentTime  < 1200: #20 hours of flying
            print(aircrafts[i].currentAirport, " => ", end='')
            ChosenAirport = choose_random_airport(CurrentAirport, HubLeg, LegNumber, aircrafts[i].hasHubbed) # Choose a random acceptable airport to fly to
            Home = nearest_home(CurrentAirport, aircrafts[i].model)

            #Get time to home and time to next leg and compare
            TimeToHome = calculate_total_flight_duration(aircrafts[i], CurrentAirport, Home, True) #Time it takes to fly home
            TimeToNextLeg += calculate_total_flight_duration(aircrafts[i], CurrentAirport, ChosenAirport, True)
            if TimeToNextLeg + CurrentTime > 1200 or TimeToHome + TimeToNextLeg + CurrentTime > 1200:
                #fly home if next leg takes too long, so if time to home and time to next leg exceeds time in day
                #take off
                for ab in airports:
                    if (airports[ab].abbreviation == aircrafts[i].currentAirport):
                        airports[ab].add_gate()
                aircrafts[i].currentAirport = Home.abbreviation
                CurrentTime += TimeToHome
                isHome = True
                #arrive
                for ab in airports:
                    if (airports[ab].abbreviation == Home.abbreviation):
                        airports[ab].remove_aircraft_type(aircrafts[i].model)
                        airports[ab].remove_gate()
                        if airports[ab].is_hub:
                            aircrafts[i].hasHubbed = True
                
            else:
                #take off to next leg
                for ab in airports:
                    if (airports[ab].abbreviation == CurrentAirport.abbreviation):
                        airports[ab].add_gate()
                aircrafts[i].currentAirport = ChosenAirport.abbreviation
                CurrentAirport = ChosenAirport
                LegNumber+=1
                #CurrentTime += 90 # 1.5 hour buffer for delays and turn around
                CurrentTime += TimeToNextLeg
                #arrive at next leg
                for ab in airports:
                    if (airports[ab].abbreviation == CurrentAirport.abbreviation):
                        airports[ab].remove_gate()
                        if airports[ab].is_hub:
                            aircrafts[i].hasHubbed = True

        print("Finished at ", CurrentAirport.abbreviation, " at ", CurrentTime)


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
            return currentAirport
        elif CurDistance > 150 and CurDistance < ShortestDistance:
            if aircraftType in airports[i].starting_aircrafts:
                #print("Found a match when looking for a home: ", aircraftType, " and ", airports[i].starting_aircrafts)
                ShortestDistance = CurDistance
                ChosenHome = airports[i]
    return ChosenHome




#Helper Function
def choose_random_airport(startAirport, HubLeg, CountToHub, HubHistory):
    if HubLeg == CountToHub and not HubHistory:
        Hubs = [2, 4, 6, 7] #Numbers of hubs
        HubNum = random.choice(Hubs)
        return airports[HubNum]
    randomAirport = airports[random.randint(1,31)]
    while randomAirport == startAirport or randomAirport.is_hub or randomAirport.available_gates == 0:
        randomAirport = airports[random.randint(1,31)]
    if great_circle(startAirport, randomAirport) <= 150 or randomAirport.available_gates == 0:
        choose_random_airport(startAirport, HubLeg, CountToHub, HubHistory)
    return randomAirport

place_aircrafts()
generate()
