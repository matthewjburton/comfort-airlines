#This file will be used to calculate a saved % of time of a flight based on the angle of the flight and the winds
#will calculate gain or loss based on wind direction + flight angle
#THIS IS NON FUNCTIONAL ATM (need to add in way to grab lat and longitude values)

import math

# Returns a float (negative for time saved, positive for time gained)
def calculatePercentage(start, end, wind=.045):

    direction = 1.0
    offset = abs((start.lat - end.lat)*69.4) #Gives latitude distance in miles
    horizontalDistance = abs((start.long-end.long)*69.4) #Gives longitiude distance in miles

    hypotenuse = math.sqrt(offset**2 + horizontalDistance**2)

    tangentPart = offset/horizontalDistance

    angle = math.atan(tangentPart)
    angle = angle*(180/math.pi)

    if angle > 90:
        angle = angle - 90

    result = angle/90

    if start.long > end.long:
        return result*wind#Time saved

    elif end.long > start.long:
        return result*wind*-1#Time lost
    else:
        return 0
