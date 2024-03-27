"""
Print the current simulation time

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Notes: Currently, no support for daylight savings time
   This class is not meant to be a stand-alone class, instead
   it will be used by the main simulation
"""
def get_time(minutesIntoTheDay):
    hours = minutesIntoTheDay // 60
    minutes = minutesIntoTheDay % 60
    days = minutesIntoTheDay // (24 * 60)
    return days, hours, minutes

def print_time(minutesIntoTheDay):
    days, hours, minutes = get_time(minutesIntoTheDay)
    return f"Day: {days}, Time: {hours:02}:{minutes:02}"