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
from flight import Flight

class Simulation:
    @staticmethod
    def run_simulation():
        airports = Simulation.create_airports_from_database()
        aircrafts = Simulation.create_aircrafts_from_database()
        timetable = Simulation.create_timetable_from_database()

        # Initialize scheduler and clock
        clock = Clock()
        schedule = Schedule(clock)
        Simulation.populate_schedule_from_timetable(schedule, timetable, aircrafts, airports)

        # Simulation loop: handle every event in the current minute, then increment the clock
        for i in range(1440):  # Simulate for a day (1440 minutes)
            currentEvents = schedule.get_events_for_minute(clock.minutes)
            for currentEvent in currentEvents:
                print(f"{clock.print_time()}: {currentEvent.execute()}")
                # Implement event handling logic here, e.g., update flight status, track aircraft, etc.
            clock.increment_clock()

    @staticmethod
    def populate_schedule_from_timetable(schedule, timetable, aircrafts, airports):
        # Populate the schedule queue with events based on the timetable
        for flight in timetable:
            departureAircraft = next((aircraft for aircraft in aircrafts if aircraft.id == flight.aircraftID), None)
            departureAirport = next((airport for airport in airports if airport.id == flight.departureAirportID), None)
            departureEvent = DepartureEvent(departureAircraft, departureAirport, flight.localDepartureTime)
            schedule.add_event(departureEvent)

            arrivalAirport = next((airport for airport in airports if airport.id == flight.destinationAirportID), None)
            arrivalEvent = ArrivalEvent(departureAircraft, arrivalAirport, flight.localArrivalTime)
            schedule.add_event(arrivalEvent)

    @staticmethod
    def create_airports_from_database():
        # Query database for airports
        db = Database()
        query = 'SELECT * FROM airports'
        dataframe = db.execute_query_to_dataframe(query)

        # Create Airport objects and store them in a list
        airports = []
        for _, row in dataframe.iterrows():
            airport = Airport(row['airport_id'], row['name'], row['abbreviation'], row['latitude'], row['longitude'], row['timezone_offset'], row['metro_population'], row['total_gates'], row['total_gates'], row['is_hub'])
            airports.append(airport)

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
    def create_timetable_from_database():
        # Query database for flights
        db = Database()
        query = 'SELECT * FROM flights'
        dataframe = db.execute_query_to_dataframe(query)

        # Create Flight objects and store them in a list
        timetable = []
        for _, row in dataframe.iterrows():
            flight = Flight(id=row['flight_id'], number=row['flight_number'], aircraftID=row['aircraft_id'], departureAirportID=row['departure_airport_id'], destinationAirportID=row['destination_airport_id'], angleOfFlight=row['angle_of_flight'], durationMinutes=row['flight_duration_minutes'], localDepartureTime=row['local_departure_time'], localArrivalTime=row['local_arrival_time'], onTimeBin=row['on_time_bin'], gateDeparture=row['gate_departure'], gateArrival=row['gate_arrival'])
            timetable.append(flight)

        return timetable