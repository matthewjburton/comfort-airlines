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

def calculate_total_population():
    # Query database for airports
    db = database.Database()
    query = 'SELECT SUM(metro_population) FROM airports'
    total_population = db.execute_query(query)
    return total_population

# Calculate total population
totalPopulation = calculate_total_population()
