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
