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
    
    set_current_airport(aircrafts[0], airports['EWR'])
    set_current_airport(aircrafts[1], airports['LAX'])
    set_current_airport(aircrafts[2], airports['DFW'])
    set_current_airport(aircrafts[3], airports['MDW'])

    def set_current_airport(aircraft, airport):
        aircraft.currentAirport = airport
        
        airport.add_aircraft_type(aircraft.model)
        airport.remove_gate()

        aircraft.hasHubbed = True

    #aircrafts[?].currentAirport = "going to paris"

    #Place the rest of the aircrafts at airports where a hub is filled up to 7 and the rest are placed randomly up to 4
    for aircraft in aircrafts:
        # Continue to the next aircraft if this aircraft has already been placed at an airport
        if aircraft.currentAirport:
            continue

        # Generate_new_timetable a random starting airport until conditions are met
        while aircraft.currentAirport is None:
            # Select a random airport
            selectedAirport = airports[random.randint(1,30)]

            # Allocate aircraft to hub
            if selectedAirport.is_hub and selectedAirport.available_gates > 4:
                selectedAirport.add_aircraft_type(aircraft.model)
                selectedAirport.remove_gate()
                aircraft.currentAirport = selectedAirport
            # Allocate aircraft to regular airport
            elif not selectedAirport.is_hub and selectedAirport.available_gates > 1:
                selectedAirport.add_aircraft_type(aircraft.model)
                selectedAirport.remove_gate()
                aircraft.currentAirport = selectedAirport

    print_starting_locations()
    def print_starting_locations():
        for aircraft in aircrafts:
            print(f"{aircraft.tailNumber}: {aircraft.currentAirport}")
        for airport in airports:
            print(f"{airport.name}: {airport.abbreviation} {airport.available_gates}")


def generate_new_timetable():
    for aircraft in aircrafts:
        print(f"\n {aircraft.tailNumber} starting")

        isHome = False
        timeToHome = 0
        currentTime = 0
        timeToNextLeg = 0 # Potential Time
        hubLeg = random.randint(0,3)
        legNumber = 0
        currentAirport = aircraft.currentAirport

        while not isHome and timeToHome + currentTime  < 1200: #20 hours of flying
            print(aircraft.currentAirport, " => ", end='')
            ChosenAirport = choose_random_airport(currentAirport, hubLeg, legNumber, aircraft.hasHubbed) # Choose a random acceptable airport to fly to
            Home = nearest_home(currentAirport, aircraft.model)

            #Get time to home and time to next leg and compare
            timeToHome = calculate_total_flight_duration(aircraft, currentAirport, Home, True) #Time it takes to fly home
            timeToNextLeg += calculate_total_flight_duration(aircraft, currentAirport, ChosenAirport, True)
            if timeToNextLeg + currentTime > 1200 or timeToHome + timeToNextLeg + currentTime > 1200:
                #fly home if next leg takes too long, so if time to home and time to next leg exceeds time in day
                #take off
                aircraft.currentAirport.add_gate()
                aircraft.currentAirport = Home.abbreviation
                currentTime += timeToHome
                isHome = True
                #arrive
                for ab in airports:
                    if (airports[ab].abbreviation == Home.abbreviation):
                        airports[ab].remove_aircraft_type(aircraft.model)
                        airports[ab].remove_gate()
                        if airports[ab].is_hub:
                            aircraft.hasHubbed = True
                
            else:
                #take off to next leg
                for ab in airports:
                    if (airports[ab].abbreviation == currentAirport.abbreviation):
                        airports[ab].add_gate()
                aircraft.currentAirport = ChosenAirport.abbreviation
                currentAirport = ChosenAirport
                legNumber+=1
                #currentTime += 90 # 1.5 hour buffer for delays and turn around
                currentTime += timeToNextLeg
                #arrive at next leg
                for ab in airports:
                    if (airports[ab].abbreviation == currentAirport.abbreviation):
                        airports[ab].remove_gate()
                        if airports[ab].is_hub:
                            aircraft.hasHubbed = True

        print("Finished at ", currentAirport.abbreviation, " at ", currentTime)


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
def choose_random_airport(startAirport, hubLeg, CountToHub, HubHistory):
    if hubLeg == CountToHub and not HubHistory:
        Hubs = [2, 4, 6, 7] #Numbers of hubs
        HubNum = random.choice(Hubs)
        return airports[HubNum]
    randomAirport = airports[random.randint(1,31)]
    while randomAirport == startAirport or randomAirport.is_hub or randomAirport.available_gates == 0:
        randomAirport = airports[random.randint(1,31)]
    if great_circle(startAirport, randomAirport) <= 150 or randomAirport.available_gates == 0:
        choose_random_airport(startAirport, hubLeg, CountToHub, HubHistory)
    return randomAirport

place_aircrafts()
generate_new_timetable()
