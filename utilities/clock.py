"""
Print the current simulation time

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Notes: Currently, no support for daylight savings time
   This class is not meant to be a stand-alone class, instead
   it will be used by the main simulation
"""
MINUTES_IN_A_DAY = 1440

def get_time(minutes):
    hours = minutes // 60
    minutes %= 60
    days = hours // 24  # Calculate days from hours, not from minutes
    hours %= 24  # Calculate remaining hours after days are removed
    return days, hours, minutes

def print_time(minutes):
    minutes += MINUTES_IN_A_DAY # Used to visually change the first day from 0 to 1
    days, hours, minutes = get_time(minutes)
    return f"Day: {days}, Time: {hours:02}:{minutes:02}"

def get_flight_time(minutes):
    _, hours, minutes = get_time(minutes)
    return f"{hours:02}:{minutes:02}"