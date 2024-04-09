"""
2 functions first one calculates the time it takes to fly and get into cruising altitude then to reach max speed

the second function gets the amount of time it takes to descend down.

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Justin Chen
"""

import math

def calculate_acceleration_time(cruisingAltitude, maxSpeed):
    timeToCruiseAltitude = (cruisingAltitude - 10000) / (250 * 1.15)  # time to ascend to cruising altitude in minutes
    timeToMaxSpeed = (maxSpeed * 0.8 / 1.15 - 280) / (25 * 1.15)  # time to accelerate to 80% of max speed in minutes
    return timeToCruiseAltitude + timeToMaxSpeed + 1

def calculate_descent_time(distance):
    if distance >= 1500:
        cruisingAltitude = 35000
    elif distance >= 350:
        cruisingAltitude = 30000
    elif distance >= 200:
        cruisingAltitude = 25000
    else:
        cruisingAltitude = 20000
    timeToCruiseAltitude = (cruisingAltitude - 10000) / (250 * 1.15)  # time to descend to cruising altitude in minutes
    timeToLand = (distance * 1.151) / (200 * 1.15)  # time to descend at 200 miles per hour in minutes
    return timeToCruiseAltitude + timeToLand + 2