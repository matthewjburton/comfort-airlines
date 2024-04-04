"""
Class responsible for implementing the menu options under the configure costs menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

import re
import json
import os

class CostMenu:
    
    """Cost Options"""
    CONFIG_FILE_PATH = 'simulation/simulation_config.json'

    @staticmethod
    def read_config():
        if os.path.exists(CostMenu.CONFIG_FILE_PATH):
            with open(CostMenu.CONFIG_FILE_PATH, 'r') as f:
                return json.load(f)
        else:
            return {}

    @staticmethod
    def write_config(config_data):
        with open(CostMenu.CONFIG_FILE_PATH, 'w') as f:
            json.dump(config_data, f)

    @staticmethod
    def configure_fuel_cost():
        config_data = CostMenu.read_config()
        while True:
            try:
                fuelCost = input('Enter the fuel cost (dollars per gallon): $')
                if CostMenu.is_valid_dollar_value(fuelCost):
                    fuelCost = float(fuelCost)  # Convert to float after validation
                    if 0 <= fuelCost:
                        # Update the fuelCost in the config data
                        config_data['fuelCost'] = fuelCost
                        CostMenu.write_config(config_data)
                        break
                    else:
                        print('Fuel cost must be a positive value.')
                else:
                    print('Fuel cost must be a dollar value with two decimal places.')
            except ValueError:
                print("Fuel cost must be a number.")

    @staticmethod
    def configure_takeoff_cost():
        config_data = CostMenu.read_config()
        while True:
            try:
                takeoffCost = input('Enter the takeoff cost (dollars per): $')
                if not CostMenu.is_valid_dollar_value(takeoffCost):
                    takeoffCost = float(takeoffCost)
                    if 0 <= takeoffCost:
                        # Update the takeoffCost in the config data
                        config_data['takeoffCost'] = takeoffCost
                        CostMenu.write_config(config_data)
                        break
                    else:
                        print('Takeoff cost must be a positive value.')
                else:
                    print('Takeoff cost must be a dollar value with two decimal places.')
            except ValueError:
                print("Takeoff cost must be a number.")

    @staticmethod
    def configure_landing_cost():
        config_data = CostMenu.read_config()
        while True:
            try:
                landingCost = input('Enter the landing cost (dollars per): $')
                if not CostMenu.is_valid_dollar_value(landingCost):
                    landingCost = float(landingCost)
                    if 0 <= landingCost:
                        # Update the landingCost in the config data
                        config_data['landingCost'] = landingCost
                        CostMenu.write_config(config_data)
                        break
                    else:
                        print('Landing cost must be a positive value.')
                else:
                    print('Landing cost must be a dollar value with two decimal places.')
            except ValueError:
                print("Landing cost must be a number.")

    @staticmethod
    def configure_aircraft_cost():
        print("\nExecuting configure_aircraft_cost()")

    def is_valid_dollar_value(input_str):
        # Regular expression to match dollar value with two decimal places
        pattern = r'^\d+\.\d{2}'
        return re.match(pattern, input_str) is not None