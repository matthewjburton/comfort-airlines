"""
Class used to represent aircraft objects in the simulation. Important for tracking the dynamic information of each aircraft

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

REQUIRES_MAINTENANCE = 0#200 # aircraft require maintenance after 200 hours of flight

class Aircraft:
    def __init__(self, id, tailNumber, name, model, maximumSpeed, maximumCapacity, maximumFuel, cargoVolume, leasingCost):
        self._id = id
        self._tailNumber = tailNumber
        self._name = name
        self._model = model
        self._maximumSpeed = maximumSpeed
        self._maximumCapacity = maximumCapacity
        self._maximumFuel = maximumFuel
        self._currentFuel = maximumFuel # Doing this costs the company, fuel cant just come from thin air
        self._cargoVolume = cargoVolume
        self._leasingCost = leasingCost
        self._timeSinceLastMaintenance = 0
        self._requiresMaintenance = False
        self._currentAirport = None
        self._hasHubbed = False

    @property
    def id(self):
        return self._id

    @property
    def currentAirport(self):
        return self._currentAirport

    @property
    def tailNumber(self):
        return self._tailNumber
    
    @property
    def hasHubbed(self):
        return self._hasHubbed

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def maximumSpeed(self):
        return self._maximumSpeed

    @property
    def maximumCapacity(self):
        return self._maximumCapacity

    @property
    def maximumFuel(self):
        return self._maximumFuel
    
    @property
    def currentFuel(self):
        return self._currentFuel

    @property
    def cargoVolume(self):
        return self._cargoVolume

    @property
    def leasingCost(self):
        return self._leasingCost

    @property
    def timeSinceLastMaintenance(self):
        return self._timeSinceLastMaintenance
    
    @timeSinceLastMaintenance.setter
    def timeSinceLastMaintenance(self, durationOfLastFlight):
        self._timeSinceLastMaintenance += durationOfLastFlight

        if self._timeSinceLastMaintenance >= (REQUIRES_MAINTENANCE * 60):
            self._requiresMaintenance = True
        else:
            self._requiresMaintenance = False

    @currentAirport.setter
    def currentAirport(self, abbreviation):
        self._currentAirport=abbreviation
    
    @hasHubbed.setter
    def hasHubbed(self, value):
        self._hasHubbed=value