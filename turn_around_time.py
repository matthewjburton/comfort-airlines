"""
Return the minimum amount of time in minutes that an aircraft must wait before taking off for its next flight

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Notes:
    This function will be in the simulation immediately after a flight lands
    Consider moving this function to an event scheduler or the aircraft class
    Consider changing the parameter passed in to simply the aircraft and access its fuel level to determine if it needs to be refueled
"""
# Time in minutes
DISEMBARK = 15          # time for passengers to disembark
CLEAN_AND_CREW = 10     # time to clean the aircraft and change the crew
BOARDING = 15           # time for passsengers to board the aircraft
REFUEL = 10             # time to refuel the aircraft

def turn_around_time(aircraftNeedsRefuel):
    # Time calculation
    turnAroundTime = DISEMBARK + CLEAN_AND_CREW + BOARDING

    # Account for refueling
    if aircraftNeedsRefuel:
        turnAroundTime += REFUEL

    return turnAroundTime