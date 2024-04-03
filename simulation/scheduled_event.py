"""
Handle various event types, storing references to the associated information

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from .schedule import Schedule
from .aircraft_objects import aircrafts
from .airport_objects import airports

MAINTENANCE_TIME = 1.5 # time in days

class ScheduledEvent:
    def __init__(self, eventType, time):
        self._event_type = eventType
        self._time = time

    def execute(self):
        # Implement the specific behavior of the event
        pass

class DepartureEvent(ScheduledEvent):
    def __init__(self, flight):
        super().__init__('Departure', flight.departureTime)
        self._aircraft = aircrafts[flight.aircraftID]
        self._airport = airports[flight.departureAirportID]

    def execute(self):
        aircraftTailNumber = self._aircraft.tailNumber
        airportAbbreviation = self._airport.abbreviation
        # if self._aircraft.currentFuel < fuel_required_for_flight(flight):
        #    raise ValueError(f"Aircraft {aircraftTailNumber} doesn't have enough fuel to reach its destination {airportAbbreviation}")
        
        #finances.charge(takeoffFee)
        return f"Aircraft {aircraftTailNumber} departing from Airport {airportAbbreviation}"        



class ArrivalEvent(ScheduledEvent):
    def __init__(self, flight):
        super().__init__('Arrival', flight.arrivalTime)
        self._flight = flight
        self._aircraft = aircrafts[flight.aircraftID]
        self._airport = airports[flight.destinationAirportID]

    def execute(self):
        aircraftTailNumber = self._aircraft.tailNumber
        airportAbbreviation = self._airport.abbreviation

        # Handle aircraft maintenance
        self._aircraft.timeSinceLastMaintenance += self._flight.duration
        if self._aircraft._requiresMaintenance:
            Schedule.get_instance().add_event(StartMaintenanceEvent(self._aircraft, self._airport, self._flight.arrivalTime))

        #self._aircraft.currentFuel -= fuel_burned_during_flight(flight)
        #finances.charge(landingFee)
        return f"Aircraft {aircraftTailNumber} arriving at Airport {airportAbbreviation}"
    


class StartMaintenanceEvent(ScheduledEvent):
    def __init__(self, aircraft, airport, arrivalTime):
        super().__init__('Start Maintenance', arrivalTime + 1)
        self._aircraft = aircraft
        self._airport = airport
        Schedule.get_instance().add_event(FinishMaintenanceEvent(self._aircraft, self._airport, arrivalTime))

    def execute(self):
        aircraftTailNumber = self._aircraft.tailNumber
        airportAbbreviation = self._airport.abbreviation

        if not self._airport._isHub:
            raise ValueError(f"Aircraft {aircraftTailNumber} can only be maintenanced at a hub airport")
        
        self._aircraft.timeSinceLastMaintenance = 0
        return f"Maintenancing aircraft {aircraftTailNumber} at Airport {airportAbbreviation}"
    



class FinishMaintenanceEvent(ScheduledEvent):
    def __init__(self, aircraft, airport, time):
        super().__init__('Finish Maintenance', time + 1 + (MAINTENANCE_TIME * 24 * 60))
        self._aircraft = aircraft
        self._airport = airport

    def execute(self):
        aircraftTailNumber = self._aircraft.tailNumber
        airportAbbreviation = self._airport.abbreviation
        
        self._aircraft.timeSinceLastMaintenance = 0
        return f"Finished maintenancing aircraft {aircraftTailNumber} at Airport {airportAbbreviation}"
    



