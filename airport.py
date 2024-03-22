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
import database

class Airport:
    def __init__(self, id, name, abbreviation,
    latitude, longitude, timezoneOffset, metroPopulation, totalGates, availableGates, isHub):

        self._id = id
        self._name = name
        self._abbreviation = abbreviation
        self._latitude = latitude
        self._longitude = longitude
        self._timezoneOffset = timezoneOffset
        self._metroPopulation = metroPopulation
        self._totalGates = totalGates
        self._availableGates = availableGates
        self._isHub = isHub

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def abbreviation(self):
        return self._abbreviation

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def timezone_offset(self):
        return self._timezoneOffset

    @property
    def metro_population(self):
        return self._metroPopulation

    @property
    def total_gates(self):
        return self._totalGates

    @property
    def available_gates(self):
        return self._availableGates
    
    def remove_gate(self):
        if self._availableGates > 0:
            self._availableGates -= 1
        else:
            raise ValueError("No available gates to remove.")

    def add_gate(self):
        if self._availableGates < self._totalGates:
            self._availableGates += 1
        else:
            raise ValueError("No available gates to add.")

    @property
    def is_hub(self):
        return self._isHub

"""
Below: Everything below is for auto generation of each Airport class instance
    this includes database connection, formatting the pandas dataframe, 
    and algorithmically creating the class objects
"""

# Query database for airports
db = database.Database()
query = 'SELECT * FROM airports'
dataframe = db.execute_query_to_dataframe(query)

# Convert columns with 0/1 values to integers
binary_columns = ['is_hub']  # Add other column names here if needed
dataframe[binary_columns] = dataframe[binary_columns].astype(int)

# Track total population or all airports
totalPopulation = 0

# Create Airport list, just to have a list of the airport objects we have, mostly for
# debugging or ease of access purposes
dataframe = dataframe.to_dict(orient='records')
airportList = []

for airport in dataframe:

    # Create Airport object using the Abbreviation as the Object name
    setattr(Airport,
            airport['abbreviation'], 
            Airport(airport['airport_id'],
            airport['name'],
            airport['abbreviation'],
            airport['latitude'],
            airport['longitude'],
            airport['timezone_offset'],
            airport['metro_population'],
            airport['total_gates'],
            airport['total_gates'],
            airport['is_hub']))

    # Update Total Population and add airport to list
    airportList.append(airport['abbreviation'])
    totalPopulation += airport['metro_population']

