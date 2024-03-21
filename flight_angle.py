"""
Returns % of base flight time that a flight will take based on wind and bearing angle

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""

import math

# Returns a float to multiply with flight time to find the actual time the flight will take
def calculate_percentage(startAirport, endAirport, wind = .045):

    dif = endAirport.longitude - startAirport.longitude

    #Edge case: Flight is perfectly vertical, wind has no effect
    if(dif == 0):
        return 1

    #Edge case: Flight is perfectly horizontal, wind has full effect
    if(startAirport.latitude == endAirport.latitude):
        if(dif < 0):
            return 1 + wind # East to West, Time added
        else:
            return 1 - wind # West to East, Time saved

    # Math to determine the bearing angle: will yield value between -180 to 180
    firstPart = math.cos(math.radians(endAirport.latitude)) * math.sin(math.radians(dif))
    secondPart = math.cos(math.radians(startAirport.latitude)) * math.sin(math.radians(endAirport.latitude)) - math.sin(math.radians(startAirport.latitude) )* math.cos(math.radians(endAirport.latitude)) * math.cos(math.radians(dif))

    degrees = math.degrees(math.atan2(firstPart,secondPart)) # degrees is the variable that will be manipulated, as it is the bearing angle between airports


    if(degrees < 0): # Flight direction is : East to West
        percentValue = degrees / 90 # Gets percentage of 90(Full wind speed) that the flight angle contains
        if(percentValue < -1): # If it is below negative one, need to do additional calculations to get correct %
            percentValue = -1 * (percentValue + 2)

        percentValue = 1 + (percentValue * -1 * wind) # Since negative number indicates % increase in flight time, change % to positive, mulitply by wind, and add one to find % of base flight time this flight will have

    else: # Flight direction is: West to East
        percentValue = degrees / 90 # Gets percentage of 90(Full wind speed) that the flight angle contains
        if (percentValue > 1): # If it is above one, need to do additional calculations to get correct %
            percentValue = (1 - percentValue) + 1

        percentValue = 1 - (percentValue * wind) # Since % number indicates % decrease in flight time, multiply % by wind, and subtract from 1 to get % time of base flight time this flight will have

    return percentValue # Multiply this result by flight time to get actual flight time accounting for wind
