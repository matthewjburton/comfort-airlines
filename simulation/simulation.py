"""
Implements the funcitonality of the user options from the Simulation section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.database import Database
from utilities.clock import print_time
from utilities.flight_duration import calculate_flight_duration

from objects.flight import Flight

from .schedule import Schedule
from .scheduled_event import DepartureEvent, ArrivalEvent
from .aircraft_objects import aircrafts
from .airport_objects import airports

import os
import json

MINUTES_IN_A_DAY = 1400
CONFIG_FILE_PATH = 'simulation/simulation_config.json'

class Simulation:
    @staticmethod
    def run_simulation():
        # load the simulation configuration dictionary
        config = Simulation.get_simulation_configuration()

        # Get instance of schedule singleton
        schedule = Schedule.get_instance()

        # Populate schedule with departure and arrival events
        schedule = Simulation.populate_schedule_from_timetable(schedule)

        # Set simulation start and end times form the simulation config
        startTime = MINUTES_IN_A_DAY * config.startDate
        endTime = MINUTES_IN_A_DAY * config.duration

        # MAIN SIMULATION LOOP, process each minute
        for minute in range(startTime, endTime):
            # Handle all events for this minute
            currentEvents = schedule.get_events_for_minute(minute)
            for currentEvent in currentEvents:
                print(f"{print_time(minute)}: {currentEvent.execute()}") 

            # Determine if it's time to generate a report, and generate one if so
            if Simulation.should_generate_report(config, minute):
                Simulation.generate_report()

    @staticmethod
    def populate_schedule_from_timetable(schedule):
        timetable = Simulation.create_timetable_from_database()

        # Populate the schedule queue with events based on the timetable
        for flightKey in timetable:
            flight = timetable[flightKey]

            schedule.add_event(DepartureEvent(flight))

            flight.duration = calculate_flight_duration(aircrafts[flight.aircraftID], airports[flight.departureAirportID], airports[flight.destinationAirportID])

            schedule.add_event(ArrivalEvent(flight))

        return schedule

    @staticmethod
    def create_timetable_from_database():
        # Query database for flights
        db = Database()
        query = 'SELECT * FROM flights'
        dataframe = db.execute_query_to_dataframe(query)

        # Create Flight objects and store them in a list
        timetable = {}
        for _, row in dataframe.iterrows():
            flight = Flight(row['flight_id'], row['flight_number'], row['aircraft_id'], row['departure_airport_id'], row['destination_airport_id'], row['angle_of_flight'], row['flight_duration_minutes'], row['local_departure_time'], row['local_arrival_time'], row['on_time_bin'], row['gate_departure'], row['gate_arrival'])
            timetable[row['flight_id']] = flight

        return timetable
    
    def get_simulation_configuration():
        if os.path.exists(CONFIG_FILE_PATH):
            with open(CONFIG_FILE_PATH, 'r') as f:
                return json.load(f)
        else:
            return {}
        
    def should_generate_report(config, minute):
        reportFrequency = config.reportFrequency
        endTime = MINUTES_IN_A_DAY * config.startDate + MINUTES_IN_A_DAY * config.duration

        if reportFrequency is 'daily' and minute % MINUTES_IN_A_DAY == 0:
            return True
        elif reportFrequency is 'weekly' and (minute / 7) % MINUTES_IN_A_DAY == 0:
            return True
        elif reportFrequency is 'monthly' and (minute / 30) % MINUTES_IN_A_DAY == 0:
            return True
        elif reportFrequency is 'yearly' and (minute / 365) % MINUTES_IN_A_DAY == 0:
            return True
        elif reportFrequency is 'final' and minute == endTime:
            return True
        else:
            return False
        
    def generate_report():
        print('Executing generate_report()')

