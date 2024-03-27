"""
Implements the funcitonality of the user options from the Simulation section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.clock import print_time
from utilities.database import Database

from objects.airport import Airport
from objects.aircraft import Aircraft
from objects.flight import Flight

from .schedule import Schedule
from .scheduled_event import DepartureEvent, ArrivalEvent

MINUTES_IN_A_DAY = 1400

class Simulation:
    @staticmethod
    def run_simulation():
        # Initialize schedule
        schedule = Schedule()
        schedule = Simulation.populate_schedule_from_timetable(schedule)

        # Simulation loop: handle every event for each minute
        for minute in range(MINUTES_IN_A_DAY):
            currentEvents = schedule.get_events_for_minute(minute)
            for currentEvent in currentEvents:
                print(f"{print_time(minute)}: {currentEvent.execute()}")       

    @staticmethod
    def populate_schedule_from_timetable(schedule):
        timetable = Simulation.create_timetable_from_database()

        # Populate the schedule queue with events based on the timetable
        for flight in timetable:
            schedule.add_event(DepartureEvent(flight))
            schedule.add_event(ArrivalEvent(flight))

    @staticmethod
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