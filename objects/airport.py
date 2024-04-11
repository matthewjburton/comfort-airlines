"""
Airport class. Used in the simulation to get and set dynamic values

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""
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
        self._inboundFlights = {}
        self._startingAircraftList = {}
        self._currentAircraftList = []
        self._lastTakeoff = -1
        self._lastLanding = -1

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

    @property
    def inbound_flights(self):
        return self._inboundFlights
    
    @property
    def starting_aircrafts(self):
        return self._startingAircraftList

    def add_aircraft_type(self, _aircraftType):
        if _aircraftType in self._startingAircraftList:
            self._startingAircraftList[_aircraftType] += 1
        else:
            self._startingAircraftList[_aircraftType] = 1

    def remove_aircraft_type(self, _aircraftType):
        if _aircraftType in self._startingAircraftList:
            if self._startingAircraftList[_aircraftType] > 1:
                self._startingAircraftList[_aircraftType] -= 1
            else:
                del self._startingAircraftList[_aircraftType]
        else:
            print("Aircraft not found. Ensure that you only remove starting aircraft types.")
    
    def add_inbound_flight(self, aircraftName, arrivalTime):
        if len(self._inboundFlights) < self._availableGates:
            self._inboundFlights.update({arrivalTime: aircraftName})
        else:
            raise ValueError("Inbound flights cannot exceed number of gates available.")

    def remove_inbound_flight(self, aircraftName, arrivalTime):
        if len(self._inboundFlights) > 0:
            self._inboundFlights.pop(arrivalTime)
        else:
            raise ValueError("Cannot remove an inbound flight from an airport with no inbound flights.")
        
    def add_aircraft(self, _aircraft):
        if _aircraft not in self._currentAircraftList:
            self._currentAircraftList.append(_aircraft)
        else:
            raise ValueError("Aircraft already in airport. Can't be added")

    def remove_aircraft(self, _aircraft):
        if _aircraft in self._currentAircraftList:
            self._currentAircraftList.remove(_aircraft)
        else:
            raise ValueError("Aircraft not in airport, cannot be removed")
        
        