"""
Create a list of airport objects used in the simulation to manage their dynamic information

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

from utilities.database import Database
from objects.airport import Airport

def create_airports_from_database():
    # Query database for airports
    db = Database()
    query = 'SELECT * FROM airports'
    dataframe = db.execute_query_to_dataframe(query)

    # Create Airport objects and store them in a list
    airports = {}
    for _, row in dataframe.iterrows():
        airport = Airport(row['airport_id'], row['name'], row['abbreviation'], row['latitude'], row['longitude'], row['timezone_offset'], row['metro_population'], row['total_gates'], row['total_gates'], int(row['is_hub']), 0)
        airports[row['airport_id']] = airport


    return airports

airports = create_airports_from_database()
