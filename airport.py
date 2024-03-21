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
"""
import database

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

# Query database for airports
db = database.Database()
query = 'SELECT * FROM airports'
dataframe = db.execute_query_to_dataframe(query)

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

