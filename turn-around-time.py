# Purpose:  Return the minimum amount of time in minutes that an
#           aircraft must wait before taking off for its next flight
# Author:   Matt Burton
# Notes:    This function will be in the simulation immediately after a flight lands
#           Consider moving this function to an event scheduler or the aircraft class

def TurnAroundTime(refueling):
    # time breakdown
    timeToDisembarkPassengers = 15
    timeToCleanAircraftAndChangeCrew = 10
    timeToBoardPassengers = 15
    timeToRefuel = 10

    # time calculation
    totalTurnAroundTime = timeToDisembarkPassengers + timeToCleanAircraftAndChangeCrew + timeToBoardPassengers
    if refueling:
        totalTurnAroundTime += timeToRefuel

    return totalTurnAroundTime