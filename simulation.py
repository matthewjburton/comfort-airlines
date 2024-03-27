"""
Implements the funcitonality of the user options from the Simulation section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from schedule import Schedule
from clock import Clock
from database import Database
from scheduled_event import DepartureEvent, ArrivalEvent
from airport import Airport
from aircraft import Aircraft

class Simulation:
    @staticmethod
    def run_simulation():
        # Initialize scheduler and clock
        clock = Clock()
        schedule = Schedule(clock)

        # Read in the airports data from the database and create Airport objects
        airports = Simulation.create_airports_from_database()

        # Read in the aircraft data from the database and create Aircraft objects
        aircrafts = Simulation.create_aircrafts_from_database()

        schedule = Simulation.populate_schedule_from_timetable(schedule)

        # Simulation loop: handle every event in the current minute, then increment the clock
        for i in range(1440):  # Simulate for a day (1440 minutes)
            current_events = schedule.get_events_for_minute(clock.minutes)
            for current_event in current_events:
                print(f"{clock.print_time()}: {current_event.execute()}")
                # Implement event handling logic here, e.g., update flight status, track aircraft, etc.
            clock.increment_clock()

    @staticmethod
    def create_airports_from_database():
        # Query database for airports
        db = Database()
        query = 'SELECT * FROM airports'
        dataframe = db.execute_query_to_dataframe(query)

        # Create Airport objects and store them in a dictionary
        airports = {}
        for _, row in dataframe.iterrows():
            airport = Airport(row['airport_id'], row['name'], row['abbreviation'], row['latitude'], row['longitude'], row['timezone_offset'], row['metro_population'], row['total_gates'], row['total_gates'], row['is_hub'])
            airports[row['abbreviation']] = airport

        return airports

    @staticmethod
    def create_aircrafts_from_database():
        # Query database for aircraft
        db = Database()
        query = 'SELECT * FROM aircraft'
        dataframe = db.execute_query_to_dataframe(query)

        # Create Aircraft objects and store them in a list
        aircrafts = []
        for _, row in dataframe.iterrows():
            aircraft = Aircraft(row['aircraft_id'], row['tail_number'], row['name'], row['model'], row['maximum_speed'], row['maximum_capacity'], row['maximum_fuel'], row['cargo_volume'], row['leasing_cost'])
            aircrafts.append(aircraft)

        return aircrafts

    @staticmethod
    def populate_schedule_from_timetable(schedule):
        # Read in the timetable from the database
        db = Database()
        query = 'SELECT * FROM flights'
        dataframe = db.execute_query_to_dataframe(query)

        # Populate the schedule queue with events based on the timetable
        for _, flight in dataframe.iterrows():
            departure_event = DepartureEvent(flight['aircraft_id'], flight['departure_airport_id'], flight['local_departure_time'])
            schedule.add_event(departure_event)
            arrival_event = ArrivalEvent(flight['aircraft_id'], flight['destination_airport_id'], flight['local_arrival_time'])
            schedule.add_event(arrival_event)

        return schedule