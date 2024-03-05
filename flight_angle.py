#Purpose: Returns % of base flight time that a flight will take based on wind and bearing angle
#Authors:  Jeremy Maas, Matt Burton, McHale Trotter, Ryan Hirscher, Kevin Sampson, Justin Chen



import math
import airport

# Returns a float to multiply with flight time to find the actual time the flight will take
def calculatePercentage(startAirport, endAirport, wind=.045):

    dif = endAirport.get_airport_longitude()-startAirport.get_airport_longitude()

    #Edge case: Flight is perfectly vertical, wind has no effect
    if(dif == 0):
        return 1

    #Edge case: Flight is perfectly horizontal, wind has full effect
    if(startAirport.get_airport_latitude() == endAirport.get_airport_latitude()):
        if(dif<0):
            return 1+wind #East to West, Time added
        else:
            return 1-wind #West to East, Time saved

    #Math to determine the bearing angle: will yield value between -180 to 180
    X = math.cos(math.radians(endAirport.get_airport_latitude())) * math.sin(math.radians(dif))
    Y = math.cos(math.radians(startAirport.get_airport_latitude())) * math.sin(math.radians(endAirport.get_airport_latitude())) - math.sin(math.radians(startAirport.get_airport_latitude()) )* math.cos(math.radians(endAirport.get_airport_latitude())) * math.cos(math.radians(dif))

    Z = math.degrees(math.atan2(X,Y))#Z is the variable that will be manipulated, as it is the bearing angle between airports


    if(Z<0): #Flight direction is : East to West
        Z = Z/90 #Gets percentage of 90(Full wind speed) that the flight angle contains
        if(Z< -1): #If it is below negative one, need to do additional calculations to get correct %
            Z = -1*(Z + 2)

        Z = 1+(Z*-1*wind)#Since negative number indicates % increase in flight time, change % to positive, mulitply by wind, and add one to find % of base flight time this flight will have

    else:#Flight direction is: West to East
        Z = Z/90#Gets percentage of 90(Full wind speed) that the flight angle contains
        if (Z > 1): #If it is above one, need to do additional calculations to get correct %
            Z = (1 - Z) + 1

        Z = 1-(Z*wind)#Since % number indicates % decrease in flight time, multiply % by wind, and subtract from 1 to get % time of base flight time this flight will have


    return Z #Multiply this result by flight time to get actual flight time accounting for wind
