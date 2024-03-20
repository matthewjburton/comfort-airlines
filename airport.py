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
            At the moment, you will need to use (airportname).(methodname) as the format
"""

import mysql.connector
import pandas as pd

class Airport:

    def __init__(self, airportID, airportName, airportAbbreviation,
    latitude, longitude, timezoneOffset, metroPopulation, totalGates, availableGates, isHub):

        self.airportID = airportID
        self.airportName = airportName
        self.airportAbbreviation = airportAbbreviation
        self.latitude = latitude
        self.longitude = longitude
        self.timezoneOffset = timezoneOffset
        self.metroPopulation = metroPopulation
        self.totalGates = totalGates
        self.availableGates = availableGates
        self.isHub = isHub

    @property
    def id(self):
        return self.airportID

    @property
    def name(self):
        return self.airportName

    @property
    def abbreviation(self):
        return self.airportAbbreviation

    @property
    def latitude(self):
        return self.latitude

    @property
    def longitude(self):
        return self.longitude

    @property
    def timezone_offset(self):
        return self.timezoneOffset

    @property
    def metro_population(self):
        return self.metroPopulation

    @property
    def total_gates(self):
        return self.totalGates

    @property
    def available_gates(self):
        return self.availableGates
    
    def remove_gate(self):
        if self.availableGates > 0:
            self.availableGates -= 1
        else:
            raise ValueError("No available gates to remove.")

    def add_gate(self):
        if self.availableGates < self.totalGates:
            self.availableGates += 1
        else:
            raise ValueError("No available gates to add.")

    @property
    def is_hub(self):
        return self.isHub

"""
Below: Everything below is for auto generation of each Airport class instance
    this includes database connection, formatting the pandas dataframe, 
    and algorithmically creating the class objects
"""

# Establish Database connection
dbConnection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Cloud9",
    database="cloudnine")

# Run base query to gather all information from airports table
query = pd.read_sql_query('''SELECT * FROM airports''', dbConnection)

# Put query results into a Pandas dataframe
dataframe = pd.DataFrame(query, columns=['airport_id', 'name', 'abbreviation', 'latitude', 'longitude',
                                        'timezone_offset', 'metro_population', 'total_gates', 'is_hub'])

# Format dataframe to remove 'b' strings using utf-8 format
dataframe['is_hub'] = dataframe['is_hub'].str.decode('utf-8')

# Convert to list of dictionaries
dataframe = dataframe.to_dict(orient='records')

# Create total_population variable to help with flight demand
totalPopulation = 0

# Create Airport list, just to have a list of the airport objects we have, mostly for
# debugging or ease of access purposes
airportList = []

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

    # Update Total Population and add airport to list
    airportList.append(x['abbreviation'])
    totalPopulation+=x['metro_population']

