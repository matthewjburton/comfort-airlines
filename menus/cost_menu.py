"""
Responsible for implementing the menu options under the configure costs menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

from utilities.database import Database

import re
import json
import os

class CostMenu:
    """Cost Options"""

    CONFIG_FILE_PATH = 'simulation/simulation_config.json'

    @staticmethod
    def read_config():
        """
        Reads the simulation configuration from the JSON file.

        Returns:
            dict: The simulation configuration.
        """
        if os.path.exists(CostMenu.CONFIG_FILE_PATH):
            with open(CostMenu.CONFIG_FILE_PATH, 'r') as f:
                return json.load(f)
        else:
            return {}

    @staticmethod
    def write_config(config):
        """
        Writes the simulation configuration to the JSON file.

        Parameters:
            config (dict): The simulation configuration to write.
        """
        with open(CostMenu.CONFIG_FILE_PATH, 'w') as f:
            json.dump(config, f)

    @staticmethod
    def configure_fuel_cost():
        """
        Configures the fuel cost for the simulation.

        Prompts the user to enter a new fuel cost and updates the configuration accordingly.
        """
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
                    # Remove commas from fuelCost
                    fuelCost = fuelCost.replace(',', '')

                    fuelCost = float(fuelCost)  # Convert to float after validation
                    if 0 <= fuelCost:
                        # Update the fuelCost in the config data
                        config['fuelCost'] = fuelCost
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Fuel cost must be a positive value.\n')
                else:
                    print('Fuel cost must be a valid dollar value.\n')
            except ValueError:
                print("Fuel cost must be a number.\n")

    @staticmethod
    def configure_takeoff_cost():
        """
        Configures the takeoff cost for the simulation.

        Prompts the user to enter a new takeoff cost and updates the configuration accordingly.
        """
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
                if CostMenu.is_valid_dollar_value(takeoffCost):
                    # Remove commas from takeoffCost
                    takeoffCost = takeoffCost.replace(',', '')

                    takeoffCost = float(takeoffCost)
                    if 0 <= takeoffCost:
                        # Update the takeoffCost in the config data
                        config['takeoffCost'] = takeoffCost
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Takeoff cost must be a positive value.\n')
                else:
                    print('Takeoff cost must be a valid dollar value.\n')
            except ValueError:
                print("Takeoff cost must be a number.\n")

    @staticmethod
    def configure_landing_cost():
        """
        Configures the landing cost for the simulation.

        Prompts the user to enter a new landing cost and updates the configuration accordingly.
        """
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
                if CostMenu.is_valid_dollar_value(landingCost):
                    # Remove commas from landingCost
                    landingCost = landingCost.replace(',', '')
                    
                    landingCost = float(landingCost)
                    if 0 <= landingCost:
                        # Update the landingCost in the config data
                        config['landingCost'] = landingCost
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Landing cost must be a positive value.\n')
                else:
                    print('Landing cost must be a valid dollar value.\n')
            except ValueError:
                print("Landing cost must be a number.\n")

    @staticmethod
    def configure_leasing_costs():
        """
        Configures the leasing costs for different aircraft models.

        Displays the current leasing costs for each model and allows the user to update them.
        """
        while True:
            dataframe = CostMenu.retrieve_aircraft_models_and_costs()
            CostMenu.display_aircraft_models_and_costs(dataframe)

            # Store models and leasing costs in a dictionary
            leasingCosts = {}
            for _, aircraft in dataframe.iterrows():
                leasingCosts[aircraft['model']] = aircraft['leasing_cost']

            model = CostMenu.handle_model_input(leasingCosts)
            
            # Handle user quitting
            if model == 'q':
                break

            # Update the leasingCosts in the config data
            config = CostMenu.read_config()
            config['leasingCost'] = leasingCosts
            CostMenu.write_config(config)

            CostMenu.handle_leasing_cost_input(model, leasingCosts, config)

            CostMenu.update_leasing_costs_in_database(leasingCosts)

    @staticmethod
    def retrieve_aircraft_models_and_costs():
        """
        Retrieves the aircraft models and their leasing costs from the database.

        Returns:
            pandas.DataFrame: DataFrame containing the aircraft models and leasing costs.
        """
        db = Database()
        query = 'SELECT DISTINCT model, leasing_cost FROM aircraft'
        dataframe = db.execute_query_to_dataframe(query)
        return dataframe
    
    @staticmethod
    def display_aircraft_models_and_costs(dataframe):
        """
        Displays the current leasing costs for each aircraft model.

        Parameters:
            dataframe (pandas.DataFrame): DataFrame containing the aircraft models and leasing costs.
        """
        print(f"\nCurrent leasing costs for each model per month:\n")
        headerDisplay = f"{'Model':<10} {'Leasing Cost':<20}\n"
        headerDisplay += f"{'':<10} {'(USD per month)':<20}\n"
        print(headerDisplay)
        for i, aircraft in dataframe.iterrows():
            aircraftDisplay = f"{aircraft['model']:<10} | ${aircraft['leasing_cost']:<20,.2f}"
            print(aircraftDisplay)
            if i == len(dataframe) - 1:
                print('')

    @staticmethod
    def handle_model_input(leasingCosts):
        """
        Handles user input for selecting an aircraft model.

        Parameters:
            leasingCosts (dict): Dictionary containing aircraft models and their leasing costs.

        Returns:
            str: The selected aircraft model.
        """
        while True:
            try:
                model = input("Enter an aircraft model or 'q' to quit: ")
                if model.lower() == 'q':
                    print('Input canceled.\n')
                    return model
                if model.upper() in leasingCosts.keys():
                    return model
                else:
                    print(f"Model '{model}' not found.\n")
            except ValueError:
                print("Model must be a string.\n")

    @staticmethod
    def handle_leasing_cost_input(model, leasingCosts, config):
        """
        Handles user input for updating the leasing cost of an aircraft model.

        Parameters:
            model (str): The aircraft model for which the leasing cost is being updated.
            leasingCosts (dict): Dictionary containing aircraft models and their leasing costs.
            config (dict): The simulation configuration.

        """
        while True:
            try:
                cost = input(f"Enter the new leasing cost for {model} or 'q' to quit: $")
                if cost.lower() == 'q':
                    print('Input canceled.\n')
                    break
                if CostMenu.is_valid_dollar_value(cost):
                    cost = float(cost.replace(',', ''))
                    if cost >= 0:
                        leasingCosts[model] = cost
                        config['leasingCost'] = leasingCosts
                        CostMenu.write_config(config)
                        break
                    else:
                        print('Leasing cost must be a positive value.\n')
                else:
                    print('Leasing cost must be a valid dollar value.\n')
            except ValueError:
                print("Leasing cost must be a number.\n")

    @staticmethod
    def update_leasing_costs_in_database(leasingCosts):
        """
        Updates the leasing costs of aircraft models in the database.

        Parameters:
            leasingCosts (dict): Dictionary containing aircraft models and their leasing costs.
        """
        db = Database()

        query = "UPDATE aircraft SET leasing_cost = CASE "
        for model, cost in leasingCosts.items():
            query += f"WHEN model = '{model}' THEN {cost} "
        query += "ELSE leasing_cost END"

        db.execute_insert_update_delete_query(query)
        
    def is_valid_dollar_value(inputString):
        """
        Checks if the input string represents a valid dollar value.

        Parameters:
            inputString (str): The input string to validate.

        Returns:
            bool: True if the input string is a valid dollar value, False otherwise.
        """
        # Regular expression to match dollar value
        pattern = r'^(?:\d{1,3}(?:,\d{3})*(?:\.\d{1,2})?|\d+(?:\.\d{1,2})?)$'
        return re.match(pattern, inputString) is not None