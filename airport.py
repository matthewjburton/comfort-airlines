"""
Pull Airport information from our database into Python Class Objects 
allowing for easier access of information.
Also adds get methods to gather specific airport information,
as well as modifying methods for more volatile data such as available gates

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas

How to use: Import airport.py in file
            Run methods as part of Airport class object.
            At the moment, you will need to use Airport.(airportname).(methodname) as the format

Example:
    import airport

    # Create an instance for JFK airport
    JFK = airport.Airport("JFK")

    # Retrieve JFK's latitude
    jfk_latitude = JFK.get_airport_latitude()
    print("JFK latitude:", jfk_latitude)

    # Modify available gates for JFK
    JFK.set_available_gates(50)

    # Retrieve updated available gates for JFK
    jfk_gates = JFK.get_available_gates()
    print("JFK available gates:", jfk_gates)
"""

import mysql.connector
import pandas as pd

class Airport:

    def __init__(self, airport_id, airport_name, airport_abbreviation,
    latitude, longitude, timezone_offset, metro_population, total_gates, available_gates, is_hub):

        self.airport_id = airport_id
        self.airport_name = airport_name
        self.airport_abbreviation = airport_abbreviation
        self.latitude = latitude
        self.longitude = longitude
        self.timezone_offset = timezone_offset
        self.metro_population = metro_population
        self.total_gates = total_gates
        self.available_gates = available_gates
        self.is_hub = is_hub

    # Below: Individual get functions. Requires airport object to be passed
    # Example: Airport.LAX.get_airport_id()
    def get_airport_id(self):
        return self.airport_id

    def get_airport_name(self):
        return self.airport_name

    def get_airport_abbreviation(self):
        return self.airport_abbreviation

    def get_airport_latitude(self):
        return self.latitude

    def get_airport_longitude(self):
        return self.longitude

    def get_airport_timezone_offset(self):
        return self.timezone_offset

    def get_metro_population(self):
        return self.metro_population

    def get_total_gates(self):
        return self.total_gates

    def get_available_gates(self):
        return self.available_gates

    def get_is_hub(self):
        return self.is_hub

    #Modifying functions below

    def remove_gate(self):
        self.available_gates -= 1

    def add_gate(self):
        self.available_gates += 1

"""
Below: Everything below is for auto generation of each Airport class instance
    this includes database connection, formatting the pandas dataframe, 
    and algorithmically creating the class objects
"""

# Establish Database connection
db_connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Cloud9",
    database="cloudnine")

# Run base query to gather all information from airports table
query = pd.read_sql_query('''SELECT * FROM airports''', db_connection)

# Put query results into a Pandas dataframe
dataframe = pd.DataFrame(query, columns=['airport_id', 'name', 'abbreviation', 'latitude', 'longitude',
                                        'timezone_offset', 'metro_population', 'total_gates', 'is_hub'])

# Format dataframe to remove 'b' strings using utf-8 format
dataframe['is_hub'] = dataframe['is_hub'].str.decode('utf-8')

# Convert to list of dictionaries
dataframe = dataframe.to_dict(orient='records')

# Change '0' to False, '1' to True for easier readability and usage
for x in dataframe:
    if x['is_hub'] == '0':
        x['is_hub'] = False 
    else:
        x['is_hub'] = True

    # Create all Airport objects using the Abbreviation as the Object name
    setattr(Airport, x['abbreviation'], Airport(x['airport_id'], x['name'], 
    x['abbreviation'], x['latitude'], x['longitude'], x['timezone_offset'], 
    x['metro_population'], x['total_gates'], x['total_gates'], x['is_hub']))
    airport_list.append(x['abbreviation'])
    total_population+=x['metro_population']

