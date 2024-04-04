"""
Class responsible for implementing the menu options under the configure simulation menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

from utilities.display_menu import display_menu
from .cost_menu import CostMenu

import json
import os

class ConfigurationMenu:
     
    """Configuration Options"""
    CONFIG_FILE_PATH = 'simulation/simulation_config.json'

    @staticmethod
    def read_config():
        if os.path.exists(ConfigurationMenu.CONFIG_FILE_PATH):
            with open(ConfigurationMenu.CONFIG_FILE_PATH, 'r') as f:
                return json.load(f)
        else:
            return {}

    @staticmethod
    def write_config(config_data):
        with open(ConfigurationMenu.CONFIG_FILE_PATH, 'w') as f:
            json.dump(config_data, f)

    @staticmethod
    def configure_start_date():
        config_data = ConfigurationMenu.read_config()
        while True:
            try:
                startDate = int(input('Enter the start date (in days): '))
                if 0 <= startDate <= 365:
                    # Update the start date in the config data
                    config_data['startDate'] = startDate
                    ConfigurationMenu.write_config(config_data)
                    break
                else:
                    print('Start date must be in the range of 0 to 365 days.')
            except ValueError:
                print("Start date must be a number.")

    @staticmethod    
    def configure_duration():
        config_data = ConfigurationMenu.read_config()
        while True:
            try:
                duration = int(input('Enter the duration (in days): '))
                if 0 <= duration <= 730:
                    # Update the duration in the config data
                    config_data['duration'] = duration
                    ConfigurationMenu.write_config(config_data)
                    break
                else:
                    print('Duration must be in the range of 0 to 730 days.')
            except ValueError:
                print("Duration must be a number.")

    @staticmethod    
    def configure_report_frequency():
        config_data = ConfigurationMenu.read_config()

        duration = config_data.get('duration', 0)
        options = ConfigurationMenu.get_report_frequency_options(duration)

        while True:
            try:
                reportFrequency = str(input(f'Enter the report frequency\n({', '.join(options)}): '))
                if reportFrequency.lower() in options:
                    # Update the report frequency in the config data
                    config_data['reportFrequency'] = reportFrequency.lower()
                    ConfigurationMenu.write_config(config_data)
                    break
                else:
                    print(f'Report frequency must be either {', '.join(options)}.')
            except ValueError:
                print("Report frequency must be a string.")

    def get_report_frequency_options(duration):
        options = ['daily']

        if duration >= 14:  # 2 weeks
            options.append('weekly')
        if duration >= 60:  # 2 months
            options.append('monthly')
        if duration >= 730:  # 2 years
            options.append('yearly')
        options.append('final')

        return options

    @staticmethod
    def configure_costs():
        print("\nExecuting configure_costs()")
        cost_options = {
                "Fuel": CostMenu.configure_fuel_cost,
                "Takeoff": CostMenu.configure_takeoff_cost,
                "Landing": CostMenu.configure_landing_cost,
                "Aircraft": CostMenu.configure_aircraft_cost
            }
        display_menu(cost_options, is_submenu=True)

    @staticmethod    
    def configure_challenges():
        print("\nExecuting configure_challenges()")
        challenge_options = {
                "View": ConfigurationMenu.view_challenges,
                "Edit": ConfigurationMenu.edit_challenges 
                }
        display_menu(challenge_options, is_submenu=True)



    """Cost Options"""
    @staticmethod
    def configure_fuel_cost():
        print("\nExecuting configure_fuel_cost()")

    @staticmethod
    def configure_gate_cost():
        print("\nExecuting configure_gate_cost()")

    @staticmethod
    def configure_takeoff_cost():
        print("\nExecuting configure_takeoff_cost()")

    @staticmethod
    def configure_landing_cost():
        print("\nExecuting configure_landing_cost()")

    @staticmethod
    def configure_aircraft_cost():
        print("\nExecuting configure_aircraft_cost()")



    """Challenge Options"""
    @staticmethod
    def view_challenges():
        print("\nExecuting view_challenges()")

    @staticmethod
    def edit_challenges():
        print("\nExecuting edit_challenges()")