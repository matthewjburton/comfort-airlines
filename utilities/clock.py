"""
Print the current simulation time

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Notes: Currently, no support for daylight savings time
   This class is not meant to be a stand-alone class, instead
   it will be used by the main simulation
"""
def get_time(minutes):
    hours = minutes // 60
    minutes = minutes % 60
    days = minutes // (24 * 60)
    return days, hours, minutes

def print_time(minutes):
    days, hours, minutes = get_time(minutes)
    return f"Day: {days}, Time: {hours:02}:{minutes:02}"