"""
Implements the funcitonality of the user options from the Simulation section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from scheduler import Scheduler
from clock import Clock
from database import Database
from event import Event
class Simulation:
    def run_simulation():
        # Initialize scheduler and clock
        clock = Clock()
        scheduler = Scheduler(clock)

        # read in the timetable
        db = Database()
        query = 'SELECT * FROM flights'
        dataframe = db.execute_query_to_dataframe(query)

        # populate the schedule queue with events based on the time table
        for flight in dataframe:
            departureEvent = Event(flight['aircraftID'], flight['airportID'], flight['departure_time'])
            scheduler.add_event(departureEvent)

        # Simulation loop: handle every event in the current minute, then increment the clock
        for i in range(1440):  # Simulate for a day (1440 minutes)
            current_events = scheduler.get_events_for_minute(clock.time)
            for event in current_events:
                print(f"Handling event: {event}")
                # Implement event handling logic here, e.g., update flight status, track aircraft, etc.
            clock.increment_clock()