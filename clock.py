"""
Manage the current simulation time

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Notes: Currently, no support for daylight savings time
   This class is not meant to be a stand-alone class, instead
   it will be used by the main simulation

Execute:  
    1. Move to the /comfort-airlines directory
    2. Execute the file using the following command in the terminal:
        python3 clock.py

"""

class Clock:
    def __init__(self):
        self.minutes = 0  # Initialize minutes

    def reset_clock(self):
        self.minutes = 0

    def increment_clock(self):
        self.minutes += 1

    def get_time(self):
        hours = self.minutes // 60
        minutes = self.minutes % 60
        days = self.minutes // (24 * 60)
        return days, hours, minutes

    def print_time(self):
        days, hours, minutes = self.get_time()
        return f"Day: {days}, Time: {hours:02}:{minutes:02}"