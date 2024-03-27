"""
Class used to represent aircraft objects in the simulation. Important for tracking the dynamic information of each aircraft

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

class Aircraft:
    def __init__(self, aircraft_id, tail_number, name, model, maximum_speed, maximum_capacity, maximum_fuel, cargo_volume, leasing_cost):
        self._aircraft_id = aircraft_id
        self._tail_number = tail_number
        self._name = name
        self._model = model
        self._maximum_speed = maximum_speed
        self._maximum_capacity = maximum_capacity
        self._maximum_fuel = maximum_fuel
        self._cargo_volume = cargo_volume
        self._leasing_cost = leasing_cost

    @property
    def aircraft_id(self):
        return self._aircraft_id

    @property
    def tail_number(self):
        return self._tail_number

    @property
    def name(self):
        return self._name

    @property
    def model(self):
        return self._model

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @property
    def maximum_capacity(self):
        return self._maximum_capacity

    @property
    def maximum_fuel(self):
        return self._maximum_fuel

    @property
    def cargo_volume(self):
        return self._cargo_volume

    @property
    def leasing_cost(self):
        return self._leasing_cost
