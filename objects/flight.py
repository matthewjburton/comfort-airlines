"""
Used to mirror the flights in the database and update their values during the simulation

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
class Flight:
    def __init__(self, id, number, aircraftID, departureAirportID, destinationAirportID,
                 angleOfFlight, duration, departureTime, arrivalTime):
        self._id = id
        self._number = number
        self._aircraftID = aircraftID
        self._departureAirportID = departureAirportID
        self._destinationAirportID = destinationAirportID
        self._angleOfFlight = angleOfFlight
        self._duration = duration
        self._departureTime = departureTime
        self._arrivalTime = arrivalTime
        self._onTimeBin = 1 # On time by default
        # self._gateDeparture = gateDeparture # Set this as the flights are scheduled
        # self._gateArrival = gateArrival # Set this as the flights are scheduled

    @property
    def id(self):
        return self.ID

    @property
    def number(self):
        return self._number

    @property
    def aircraftID(self):
        return self._aircraftID

    @property
    def departureAirportID(self):
        return self._departureAirportID

    @property
    def destinationAirportID(self):
        return self._destinationAirportID

    @property
    def angleOfFlight(self):
        return self._angleOfFlight

    @property
    def duration(self):
        return self._duration
    
    @duration.setter
    def duration(self, duration):
        self._duration = duration
        self._arrivalTime = self._departureTime + duration

    @property
    def departureTime(self):
        return self._departureTime

    @property
    def arrivalTime(self):
        return self._arrivalTime
    
    @arrivalTime.setter
    def arrivalTime(self, newArrivalTime):
        if newArrivalTime > self._arrivalTime:
            self._onTimeBin = 0 # flight has been delayed

        self._arrivalTime = newArrivalTime

    @property
    def onTimeBin(self):
        return self._onTimeBin

    @property
    def gateDeparture(self):
        return self._gateDeparture

    @property
    def gateArrival(self):
        return self._gateArrival
