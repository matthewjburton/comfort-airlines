"""
Create a list of aircraft objects used in the simulation to manage their dynamic information

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from utilities.database import Database
from objects.aircraft import Aircraft

def create_aircrafts_from_database():
    # Query database for aircraft
    db = Database()
    query = 'SELECT * FROM aircraft'
    dataframe = db.execute_query_to_dataframe(query)

    # Create Aircraft objects and store them in a list
    aircrafts = {}
    for _, row in dataframe.iterrows():
        aircraft = Aircraft(row['aircraft_id'], row['tail_number'], row['name'], row['model'], row['maximum_speed'], row['maximum_capacity'], row['maximum_fuel'], row['cargo_volume'], row['leasing_cost'])
        aircrafts[row['aircraft_id']] = aircraft

    return aircrafts

aircrafts = create_aircrafts_from_database()