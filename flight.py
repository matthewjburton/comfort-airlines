"""
Flight class used to mirror the flights in the database and update their values during the simulation

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
class Flight:
    def __init__(self, id, number, aircraftID, departureAirportID, destinationAirportID,
                 angleOfFlight, durationMinutes, localDepartureTime, localArrivalTime,
                 onTimeBin, gateDeparture, gateArrival):
        self._id = id
        self._number = number
        self._aircraftID = aircraftID
        self._departureAirportID = departureAirportID
        self._destinationAirportID = destinationAirportID
        self._angleOfFlight = angleOfFlight
        self._durationMinutes = durationMinutes
        self._localDepartureTime = localDepartureTime
        self._localArrivalTime = localArrivalTime
        self._onTimeBin = onTimeBin
        self._gateDeparture = gateDeparture
        self._gateArrival = gateArrival

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
    def durationMinutes(self):
        return self._durationMinutes

    @property
    def localDepartureTime(self):
        return self._localDepartureTime

    @property
    def localArrivalTime(self):
        return self._localArrivalTime

    @property
    def onTimeBin(self):
        return self._onTimeBin

    @property
    def gateDeparture(self):
        return self._gateDeparture

    @property
    def gateArrival(self):
        return self._gateArrival
