"""
Implements the funcitonality of the user options from the Simulation section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.clock import print_time
from utilities.database import Database
from .schedule import Schedule
from objects.airport import Airport
from objects.aircraft import Aircraft

MINUTES_IN_A_DAY = 1400

class Simulation:
    @staticmethod
    def run_simulation():
        # Initialize schedule
        schedule = Schedule()

        # Simulation loop: handle every event for each minute
        for minute in range(MINUTES_IN_A_DAY):
            currentEvents = schedule.get_events_for_minute(minute)
            for currentEvent in currentEvents:
                print(f"{print_time(minute)}: {currentEvent.execute()}")        

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
    
airports = Simulation.create_airports_from_database()
aircrafts = Simulation.create_aircrafts_from_database()