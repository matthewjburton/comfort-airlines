#Purpose: Returns % of base flight time that a flight will take based on wind and bearing angle
#Author:  Jeremy Maas
#Notes:   Airport class is temporary
#         Example usages shown below


import math

class Airport:#Temp Airport class
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

# Returns a float to multiply with flight time to find the actual time the flight will take
def calculatePercentage(startAirport, endAirport, wind=.045):

    dif = endAirport.longitude-startAirport.longitude

    #Edge case: Flight is perfectly vertical, wind has no effect
    if(dif == 0):
        return 1

    #Edge case: Flight is perfectly horizontal, wind has full effect
    if(startAirport.latitude == endAirport.latitude):
        if(dif<0):
            return 1+wind #East to West, Time added
        else:
            return 1-wind #West to East, Time saved

    #Math to determine the bearing angle: will yield value between -180 to 180
    X = math.cos(math.radians(endAirport.latitude)) * math.sin(math.radians(dif))
    Y = math.cos(math.radians(startAirport.latitude)) * math.sin(math.radians(endAirport.latitude)) - math.sin(math.radians(startAirport.latitude) )* math.cos(math.radians(endAirport.latitude)) * math.cos(math.radians(dif))

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

#Test Airports below

JFK = Airport(40.641766, -73.780968)
LAX = Airport(33.9416, -118.4085)
ORD = Airport(41.978611, -87.904724)
DFW = Airport(32.89748, -97.040443)
KC = Airport(39.099912,-94.581213)
SL = Airport(38.627089,-90.200203)
CHI = Airport(41.8781,-87.6298)
MEM = Airport(35.1495,-90.0490)

print(f"% of base flight time based on wind for JFK and LAX:")
print(calculatePercentage(JFK, LAX))
print(f"% of base flight time based on wind for JFK and ORD:")
print(calculatePercentage(JFK, ORD))
print(f"% of base flight time based on wind for JFK and DFW:")
print(calculatePercentage(JFK, DFW))
print(f"% of base flight time based on wind for KC and SL:")
print(calculatePercentage(KC, SL))
print(f"% of base flight time based on wind for CHI and MEM:")
print(calculatePercentage(CHI, MEM))

