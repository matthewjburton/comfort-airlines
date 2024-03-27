"""
Handle various event types, storing references to the associated information

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from database import Database
class ScheduledEvent:
    def __init__(self, eventType, time):
        self.event_type = eventType
        self.time = time

    def execute(self):
        # Implement the specific behavior of the event
        pass

class DepartureEvent(ScheduledEvent):
    def __init__(self, aircraft, airport, departureTime):
        super().__init__('Departure', departureTime)
        self.aircraft = aircraft
        self.airport = airport

    def execute(self):
        aircraftTailNumber = self.aircraft.tailNumber
        airportAbbreviation = self.airport.abbreviation
        return f"Aircraft {aircraftTailNumber} departing from Airport {airportAbbreviation}"        

class ArrivalEvent(ScheduledEvent):
    def __init__(self, aircraft, airport, arrivalTime):
        super().__init__('Arrival', arrivalTime)
        self.aircraft = aircraft
        self.airport = airport

    def execute(self):
        aircraftTailNumber = self.aircraft.tailNumber
        airportAbbreviation = self.airport.abbreviation
        return f"Aircraft {aircraftTailNumber} arriving at Airport {airportAbbreviation}"   
