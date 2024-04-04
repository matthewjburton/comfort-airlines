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
    def write_config(config):
        with open(CostMenu.CONFIG_FILE_PATH, 'w') as f:
            json.dump(config, f)

    @staticmethod
    def configure_fuel_cost():
        config = CostMenu.read_config()

        # Configuration information for fuel cost
        print(f"\nConfigure Fuel Cost\n===================\nSet the cost of fuel per gallon\nCurrent fuel cost: ${config.get('fuelCost', 'N/A')} per gallon\n")

        while True:
            try:
                # Prompt and store user input
                fuelCost = input("Enter the new fuel cost or 'q' to quit: $")

                # Handle user canceling
                if fuelCost.lower() == 'q':
                    print('Input canceled.\n')
                    break

                # Validate input
                if CostMenu.is_valid_dollar_value(fuelCost):
                    fuelCost = float(fuelCost)  # Convert to float after validation
                    if 0 <= fuelCost:
                        # Update the fuelCost in the config data
                        config['fuelCost'] = fuelCost
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Fuel cost must be a positive value.\n')
                else:
                    print('Fuel cost must be a dollar value with two decimal places.\n')
            except ValueError:
                print("Fuel cost must be a number.\n")

    @staticmethod
    def configure_takeoff_cost():
        config = CostMenu.read_config()

        # Configuration information for takeoff cost
        print(f"\nConfigure Takeoff Cost\n======================\nSet the cost per each aircraft takeoff\nCurrent takeoff cost: ${config.get('takeoffCost', 'N/A'):,} per takeoff\n")

        while True:
            try:
                takeoffCost = input("Enter the takeoff cost or 'q' to quit: $")

                # Handle user canceling
                if takeoffCost.lower() == 'q':
                    print('Input canceled.\n')
                    break
                    
                # Validate input
                if not CostMenu.is_valid_dollar_value(takeoffCost):
                    takeoffCost = float(takeoffCost)
                    if 0 <= takeoffCost:
                        # Update the takeoffCost in the config data
                        config['takeoffCost'] = takeoffCost
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Takeoff cost must be a positive value.\n')
                else:
                    print('Takeoff cost must be a dollar value with two decimal places.\n')
            except ValueError:
                print("Takeoff cost must be a number.\n")

    @staticmethod
    def configure_landing_cost():
        config = CostMenu.read_config()

        # Configuration information for takeoff cost
        print(f"\nConfigure Landing Cost\n======================\nSet the cost per each aircraft landing\nCurrent landing cost: ${config.get('landingCost', 'N/A'):,} per landing\n")

        while True:
            try:
                landingCost = input("Enter the landing cost or 'q' to quit: $")

                # Handle user canceling
                if landingCost.lower() == 'q':
                    print('Input canceled.\n')
                    break

                #Validate input
                if not CostMenu.is_valid_dollar_value(landingCost):
                    landingCost = float(landingCost)
                    if 0 <= landingCost:
                        # Update the landingCost in the config data
                        config['landingCost'] = landingCost
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Landing cost must be a positive value.\n')
                else:
                    print('Landing cost must be a dollar value with two decimal places.\n')
            except ValueError:
                print("Landing cost must be a number.\n")

    @staticmethod
    def configure_aircraft_cost():
        print("\nExecuting configure_aircraft_cost()")

    def is_valid_dollar_value(input_str):
        # Regular expression to match dollar value with two decimal places
        pattern = r'^\d+\.\d{2}'
        return re.match(pattern, input_str) is not None