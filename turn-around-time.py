"""
Return the minimum amount of time in minutes that an aircraft must wait before taking off for its next flight

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Notes:
    This function will be in the simulation immediately after a flight lands
    Consider moving this function to an event scheduler or the aircraft class
"""

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