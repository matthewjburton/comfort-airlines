"""
Stores a list of all events and at what times they occur. Also, resolves conlficts between invalid event addtions

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from database import Database
from flight import Flight
from scheduled_event import DepartureEvent, ArrivalEvent

class Schedule:
    def __init__(self):
        self._schedule = {}
        populate_schedule_from_timetable(self)

    def add_event(self, event):
        """
        Add an event to the scheduler.
        """
        minute = event.time  # Assuming event.time represents minutes
        if minute not in self._schedule:
            self._schedule[minute] = []  # Create a list for events at this minute if it doesn't exist
        self._schedule[minute].append(event)  # Add the event to the list for this minute

    def get_events_for_minute(self, minute):
        """
        Retrieve events scheduled for a given minute.
        """
        return self._schedule.get(minute, [])  # Return the list of events for the given minute, or an empty list if no events
    
def populate_schedule_from_timetable(self):
    timetable = create_timetable_from_database()

    # Populate the schedule queue with events based on the timetable
    for flight in timetable:
        self.add_event(DepartureEvent(flight))
        self.add_event(ArrivalEvent(flight))

def create_timetable_from_database():
    # Query database for flights
    db = Database()
    query = 'SELECT * FROM flights'
    dataframe = db.execute_query_to_dataframe(query)

    # Create Flight objects and store them in a list
    timetable = []
    for _, row in dataframe.iterrows():
        flight = Flight(id=row['flight_id'], number=row['flight_number'], aircraftID=row['aircraft_id'], departureAirportID=row['departure_airport_id'], destinationAirportID=row['destination_airport_id'], angleOfFlight=row['angle_of_flight'], duration=row['flight_duration_minutes'], localDepartureTime=row['local_departure_time'], localArrivalTime=row['local_arrival_time'], onTimeBin=row['on_time_bin'], gateDeparture=row['gate_departure'], gateArrival=row['gate_arrival'])
        timetable.append(flight)

    return timetable

