"""
Airport class. Used in the simulation to get and set dynamic values

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""
class Airport:
    def __init__(self, id, name, abbreviation,
    latitude, longitude, timezoneOffset, metroPopulation, totalGates, availableGates, isHub, inboundFlights):

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
        self._inboundFlights = inboundFlights
        self._startingAircraftList = {}
        self._reservedTimeline = {}
        self._gatei = 1

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
    
    @property
    def gatei(self):
        return self._gatei
    
    #while not airport[i].is_gate_available(arrival to departure):
    #   choose new airport
    #reserve_gate() 
    def reserve_gate(self, startTime, endTime):
        self._reservedTimeline[self._gatei] = (startTime, endTime)
        #print( self._reservedTimeline)
        self._gatei += 1
    
    @gatei.setter
    def gatei(self, gateNum):
        self.gatei = gateNum

    def is_gate_available(self, chosenArrivalTime, chosenDepartureTime):
        # Iterate through the timeline and get a count of how many gates are available, return true if there is at least one gate available
        excludeGateCount = 0
        for i in range(1,self._gatei):
            # If the query time window overlaps with a reserved time, exclude 1 gate
            startReserved, endReserved = self._reservedTimeline[i]
            if (chosenArrivalTime >= startReserved and chosenArrivalTime <= endReserved) or (chosenDepartureTime <= endReserved and chosenDepartureTime >= startReserved):
                excludeGateCount += 1
        #If there is an available gate during the chosen time window, we can land
        if self._totalGates - excludeGateCount > 0:
            return True
        else:
            return False


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
    
    def add_inbound_flight(self):
        if self._inboundFlights < self._availableGates:
            self._inboundFlights += 1
        else:
            raise ValueError("Inbound flights cannot exceed number of gates available.")

    def remove_inbound_flight(self):
        if self._inboundFlights > 0:
            self._inboundFlights -= 1
        else:
            raise ValueError("Cannot remove an inbound flight from an airport with no inbound flights.")