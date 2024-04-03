"""
Implements the funcitonality of the user options from the Timetable section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.database import Database
from utilities.flight_duration import calculate_flight_duration
from simulation.aircraft_objects import aircrafts
from simulation.airport_objects import airports
from utilities.clock import get_flight_time

class Timetable:
    def view_timetable():
        # Query the database for the routes table
        db = Database()
        query = 'SELECT * FROM flights'
        flights = db.execute_query_to_dataframe(query)

        if not flights.empty:
            Timetable.print_timetable_header()

            for _, flight in flights.iterrows():
                flight['duration'] = calculate_flight_duration(aircrafts[flight['aircraft_id']], airports[flight['departure_airport_id']], airports[flight['destination_airport_id']])
                flight['arrival_time'] = flight['departure_time'] + flight['duration']
                
                Timetable.print_flight(flight)


    def print_timetable_header():
        flightDisplay = '{:<15} | {:<20} | {:<20} | {:<20} | {:<20} | {:<10}'.format('Flight Number', 'Departure Airport', 'Destination Airport', 'Departure Time', 'Arrival Time', 'Duration')
        print(flightDisplay)

    def print_flight(flight):
        departure_time = get_flight_time(flight['departure_time'])
        arrival_time = get_flight_time(flight['arrival_time'])
        duration = get_flight_time(flight['duration'])

        flightDisplay = '{:<15} | {:<20} | {:<20} | {:<20} | {:<20} | {:<10}'.format(flight['flight_number'], airports[flight['departure_airport_id']]._abbreviation, airports[flight['destination_airport_id']]._abbreviation, departure_time, arrival_time, duration)
        print(flightDisplay)


        