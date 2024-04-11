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
            airports[ab].reserve_gate(0,0)
            aircrafts[1].addHistory(airports[ab])
        aircrafts[1].currentAirport = "EWR"
        aircrafts[1].hasHubbed = True
    aircrafts[2].currentAirport = "LAX"
    for ab in airports:
        if (airports[ab].abbreviation == "LAX"):
            airports[ab].add_aircraft_type(aircrafts[2].model)
            airports[ab].reserve_gate(0,0)
            aircrafts[2].addHistory(airports[ab])
        aircrafts[2].currentAirport = "LAX"
        aircrafts[2].hasHubbed = True 
    aircrafts[3].currentAirport = "DFW"
    for ab in airports:
        if (airports[ab].abbreviation == "DFW"):
            airports[ab].add_aircraft_type(aircrafts[3].model)
            airports[ab].reserve_gate(0,0)
            aircrafts[3].addHistory(airports[ab])
        aircrafts[3].currentAirport = "DFW"
        aircrafts[3].hasHubbed = True    
    aircrafts[4].currentAirport = "MDW"
    for ab in airports:
        if (airports[ab].abbreviation == "MDW"):
            airports[ab].add_aircraft_type(aircrafts[4].model)
            airports[ab].reserve_gate(0,0)
            aircrafts[4].addHistory(airports[ab])
        aircrafts[4].currentAirport = "MDW"
        aircrafts[4].hasHubbed = True
    #aircrafts[?].currentAirport = "going to paris" NEED TO IMPLEMENT
    i = 5
    #Place the rest of the aircrafts at airports where a hub is filled up to 7 and the rest are placed randomly up to 4
    for i in aircrafts:
        # Abbreviations in aircrafts are initialized to aaa.
        # Generate a random starting airprot until it finds an available gate
        while aircrafts[i].currentAirport == "aaa":
            ChoiceAirport = airports[random.randint(1,30)] #randomAirport.is_gate_available(arrivalTimeAtNew, departureTimeAtNew)
            if ChoiceAirport.is_gate_available(0,0):
                for ab in airports:
                    if (airports[ab].abbreviation == ChoiceAirport.abbreviation):
                        airports[ab].add_aircraft_type(aircrafts[i].model) #Add Starting Model type
                        airports[ab].reserve_gate(0,0) #Take gate at 0 and take off
                        aircrafts[i].addHistory(airports[ab]) #Add to history of flight path to avoid flying back here unless its a home
                aircrafts[i].currentAirport = ChoiceAirport.abbreviation
    #for x in aircrafts:
    #    print(x, ":", aircrafts[x].currentAirport, " ")
    #for x in airports:
    #    print(x, ":", airports[x].abbreviation, " ", airports[x].available_gates, " ")

# This code generates an aircrafts flight path for the entire day reserving gates for arrival and departure building a knowledge base
# The first aircrafts will have priority in choosing their flight path while the following aircrafts beome more and more limited
# This is the main driver of the timetable and assumes that aircrafts are placed at airports
def generate():
    for i in aircrafts:
        print("\n", aircrafts[i].tailNumber, "starting")
        # Initialize for each aircraft
        isHome = False
        CurrentTime = 0 # Clock
        TimeToNextLeg = 0 # Potential Time
        TimeToHome = 0 # Potential Time
        LegNumber = 0
        aircrafts[i].hubLeg = random.randint(0,2) # Choose the leg that will force an aicraft to go to a hub if it does not have one in its path already
        for ab in airports:
            if airports[ab].abbreviation == aircrafts[i].currentAirport:
                CurrentAirport = airports[ab] #Keep track of CurrentAirport
        while not isHome and TimeToNextLeg + CurrentTime  < 1000: #20 hours of flying is 1200, but we want to end the day early for delays
            for ab in airports:
                if airports[ab].abbreviation == aircrafts[i].currentAirport:
                    hab = airports[ab].is_hub
            print(aircrafts[i].currentAirport, hab, " => ", end='')

            # Choose the next leg in the airport, the nearest home, and the nearst home from the next airport
            # Return the airport object of the chosen
            ChosenAirport = choose_random_airport(CurrentAirport, LegNumber, aircrafts[i], CurrentTime) # Choose a random acceptable airport to fly to
            Home = nearest_home(CurrentAirport, aircrafts[i].model)
            NextHome = nearest_home(ChosenAirport, aircrafts[i].model)

            # Get time to home from current airport, time to home from next airport, and time to the next chosen airport
            # Return the minutes it takes
            TimeToHome = calculate_total_flight_duration(aircrafts[i], ChosenAirport, Home, True) #Time it takes to fly home
            TimeToNextLeg = calculate_total_flight_duration(aircrafts[i], CurrentAirport, ChosenAirport, True)
            TimeToNextHome = calculate_total_flight_duration(aircrafts[i], ChosenAirport, NextHome, True)
            if TimeToNextHome + TimeToNextLeg + CurrentTime > 1000 or TimeToNextLeg + CurrentTime > 1000 or TimeToNextHome + CurrentTime > 1000:
                # Fly home if next leg and next home time exceeds current time or if the time to the next leg + current time exceeds 1200
                # This section is for either "Flying Home" or "Staying where it is"
                # Flying Home does NOT need to check for gate availability, it can wait on the tarmac until available.
                # It is logically impossible to choose a home that will not have a gate available. The number of aicrafts will always equal the number of models at the end of the day

                #print("CHECKING: ", CurrentAirport.abbreviation, Home.abbreviation)
                
                # Arrive at Home
                CurrentTime += TimeToHome # TimeToHome can be zero if staying
                CurrentAirport = Home # Home may already equal CurrentAirport
                LegNumber+=1
                aircrafts[i].currentAirport = CurrentAirport.abbreviation
                isHome = True
                # Check if home can be hubbed and delete model type from airport
                for ab in airports:
                    if airports[ab].abbreviation == aircrafts[i].currentAirport:
                        airports[ab].remove_aircraft_type(aircrafts[i].model)
                        if airports[ab].is_hub:
                            aircrafts[i].hasHubbed = True
                
            else:
                # Take off to the next leg in the flight path
                TimeToHome = TimeToNextHome #TimeToHome is already chosen

                # Reserve the gate for the already validated time
                for ab in airports:
                    if airports[ab].abbreviation == CurrentAirport.abbreviation:
                        airports[ab].reserve_gate(CurrentTime + TimeToNextLeg, CurrentTime + TimeToNextLeg + turn_around_time(True) + WAITBUFFER)

                # Arrive at next leg airport
                aircrafts[i].currentAirport = ChosenAirport.abbreviation     
                CurrentAirport = ChosenAirport               
                aircrafts[i].addHistory(CurrentAirport.abbreviation) # Since placing the aircraft adds the first airport we add the new airport to history
                LegNumber+=1
                CurrentTime += turn_around_time(True) + WAITBUFFER
                CurrentTime += TimeToNextLeg
                for ab in airports:
                    if airports[ab].abbreviation == CurrentAirport.abbreviation and airports[ab].is_hub:
                        aircrafts[i].hasHubbed = True
        if (CurrentTime <= 1200):
            print(CurrentAirport.abbreviation, "Done.", CurrentTime)
        else:
            print(CurrentAirport.abbreviation, "Done.", CurrentTime, " LANDING LATE!!!")

# At the end of the day an airport must land at an acceptable starting airport
# We must have the next day start with the same type of aircraft at each airport
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

# Choose a random airport that meets the criteria:
    # airport must not be itself, or in flight path history
    # airport must not be a hub - Have at most one aicraft fly through one hub? Or should we change this?
    # airport must have an available gate when it lands to when it takes off
    # airport must be greater than 150 miles
    # if it is the aircrafts hub leg, it must fly to one of the 4 hubs, if all the gates at all hubs are taken, skip the hub and choose a random airport and increment hub leg
def choose_random_airport(startAirport, CountToHub, aircraft, CurrentTime):
    if aircraft.hubLeg == CountToHub and not aircraft.hasHubbed:
        Hubs = [2, 4, 6, 7] #Numbers of hubs
        for i in range(0,4):
            # Generate time window from start airport to hub
            arrivalTimeAtNew = calculate_total_flight_duration(aircraft, startAirport, airports[Hubs[i]], True) + CurrentTime #Time it arrives at Hub
            departureTimeAtNew = arrivalTimeAtNew +  turn_around_time(True) + WAITBUFFER #Time it leaves from Hub

            # Check gate availability
            if (airports[Hubs[i]].is_gate_available(arrivalTimeAtNew, departureTimeAtNew)):
                return airports[Hubs[i]] # If available, take the flight

        # If no gates available, increment and then choose a random airport
        aircraft.hubLeg += 1

    # Choose an airprot and generate time window from start airport to new chosen airport
    randomAirport = airports[random.randint(1,30)]
    arrivalTimeAtNew = calculate_total_flight_duration(aircraft, startAirport, randomAirport, True) + CurrentTime #Time it arrives at new airport
    departureTimeAtNew = arrivalTimeAtNew + turn_around_time(True) + WAITBUFFER #Time it leaves from new airport

    # While not meeting criteria, generate new airport
        #if no gate is available
        #if the random airport is the starting airport
        #if the random airport is a hub (which is not the hub leg)
        #if the random airport is in the history of the flight path of the aircraft
        #if the random airport distance is within 150 miles
    while not randomAirport.is_gate_available(arrivalTimeAtNew, departureTimeAtNew) or randomAirport.abbreviation == startAirport.abbreviation or randomAirport.is_hub or aircraft.isInHistory(randomAirport.abbreviation) or great_circle(startAirport, randomAirport) <= 150:
        randomAirport = airports[random.randint(1,30)]
        arrivalTimeAtNew = calculate_total_flight_duration(aircraft, startAirport, randomAirport, True) + CurrentTime #Time it arrives at new airport
        departureTimeAtNew = arrivalTimeAtNew +  turn_around_time(True) + WAITBUFFER #Time it leaves from new airport

    return randomAirport

place_aircrafts()
generate()
