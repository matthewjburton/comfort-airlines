
"""
Returns the time in minutes on how long it will take in minutes to travel from one airport to another depending on the aircraft model

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.great_circle import great_circle
from utilities.flight_angle import calculate_percentage
from utilities.turn_around_time import turn_around_time

PERCENT_OF_MAX_SPEED = 0.9
DEBUGGING = False

# This function calculates the estimated flight time based on departure and destination airport coordinates, and aircraft model.
def calculate_flight_duration(aircraft, departureAirport, destinationAirport):

    reducedSpeed = aircraft.maximumSpeed * PERCENT_OF_MAX_SPEED

    distance = great_circle(departureAirport, destinationAirport)

    angleFactor = calculate_percentage(departureAirport, destinationAirport)

    flightSpeed = reducedSpeed * angleFactor

    flightDuration = distance / flightSpeed
    flightDurationInMinutes = int(flightDuration * 60)
    
    if DEBUGGING:
        print(f"Maximum Speed: {aircraft.maximumSpeed:.2f} mph")
        print(f"Reduced Speed (90% of Max): {reducedSpeed:.2f} mph")
        print(f"Distance: {distance:.2f} miles")
        print(f"Angle Factor: {angleFactor:.2f}")
        print(f"Flight Speed: {flightSpeed:.2f} mph")
        print(f"Flight Duration: {flightDuration:.2f} hours")
        print(f"Flight Duration in Minutes: {flightDurationInMinutes:.2f} minutes")
    
    return flightDurationInMinutes

def calculate_total_flight_duration(aircraft, departureAirport, destinationAirport, refueling = False):
    takeOffTime = 0 #take_off_time()
    flightDuration = calculate_flight_duration(aircraft, departureAirport, destinationAirport)
    turnAroundTime = turn_around_time(refueling)

    total_flight_time = takeOffTime + flightDuration + turnAroundTime
    return total_flight_time
