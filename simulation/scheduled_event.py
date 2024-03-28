"""
Handle various event types, storing references to the associated information

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from .aircraft_objects import aircrafts
from .airport_objects import airports

class ScheduledEvent:
    def __init__(self, eventType, time):
        self.event_type = eventType
        self.time = time

    def execute(self):
        # Implement the specific behavior of the event
        pass

class DepartureEvent(ScheduledEvent):
    def __init__(self, flight):
        super().__init__('Departure', flight.localDepartureTime)
        self.aircraft = aircrafts[flight.aircraftID]
        self.airport = airports[flight.departureAirportID]

    def execute(self):
        #finances.charge(takeoffFee)

        aircraftTailNumber = self.aircraft.tailNumber
        airportAbbreviation = self.airport.abbreviation
        return f"Aircraft {aircraftTailNumber} departing from Airport {airportAbbreviation}"        

class ArrivalEvent(ScheduledEvent):
    def __init__(self, flight):
        super().__init__('Arrival', flight.localArrivalTime)
        self.flight = flight
        self.aircraft = aircrafts[flight.aircraftID]
        self.airport = airports[flight.destinationAirportID]

    def execute(self):
        #self.aircraft.currentFuel -= fuel_burned_during_flight(flight)
        self.aircraft.timeSinceLastMaintenance += self.flight.duration
        #finances.charge(landingFee)
        
        aircraftTailNumber = self.aircraft.tailNumber
        airportAbbreviation = self.airport.abbreviation
        return f"Aircraft {aircraftTailNumber} arriving at Airport {airportAbbreviation}"   
