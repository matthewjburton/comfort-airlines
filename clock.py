# Purpose:  Track the current simulation time and
#           manage incrementing time minute by minute
# Author:   Matt Burton
# Notes:    Currently, no support for daylight savings time
#           This class is not meant to be a stand-alone class, instead
#           it will be used by the main simulation
# Execute:  1. Move to the /comfort-airlines directory
#           2. Execute the file using the following command in the terminal:
#               python3 clock.py

class Clock:
    def __init__(self):
        self.time = (1, 0, 0)  # (day, hour, minute)

    def ResetClock(self):
        self.time = (1, 0, 0)

    def IncrementClock(self):
        day, hour, minute = self.time # temporarily breakdown time into its parts
        
        # incrememnt the clock by one
        if minute < 59:
            minute += 1
        elif hour < 23:
            hour += 1
            minute = 0
        else:
            day += 1
            hour = 0
            minute = 0
        
        # set the time with the updated value(s)
        self.time = (day, hour, minute)
    
    def PrintTime(self):
        day, hour, minute = self.time # temporarily breakdown time into its parts

        print("Day:" + str(day) + " " + str(hour) + ":" + str(minute))

clock = Clock() # create a new clock object

# test the incrementing and output for a single day
for i in range(0,1441):
    clock.PrintTime()
    clock.IncrementClock()
