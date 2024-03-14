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

    # Below: Individual get functions. Requires airport object to be passed
    # Example: Airport.LAX.get_airport_id()
    def get_airport_id(self):
        return self.airportID

    def get_airport_name(self):
        return self.airportName

    def get_airport_abbreviation(self):
        return self.airportAbbreviation

    def get_airport_latitude(self):
        return self.latitude

    def get_airport_longitude(self):
        return self.longitude

    def get_airport_timezone_offset(self):
        return self.timezoneOffset

    def get_metro_population(self):
        return self.metroPopulation

    def get_total_gates(self):
        return self.totalGates

    def get_available_gates(self):
        return self.availableGates

    def get_is_hub(self):
        return self.isHub

    #Modifying functions below

    def remove_gate(self):
        self.availableGates -= 1

    def add_gate(self):
        self.availableGates += 1

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

