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
    def write_config(config):
        with open(ConfigurationMenu.CONFIG_FILE_PATH, 'w') as f:
            json.dump(config, f)

    @staticmethod
    def configure_start_date():
        config = ConfigurationMenu.read_config()

        # Configuration information for start date
        print(f"\nConfigure Start Date\n====================\nSet the day that the simulation starts on\nCurrent start date: day {config.get('startDate', 'N/A'):,}\n")
        
        while True:
            try:
                # Prompt and store user input
                startDate = input("\nEnter the new start date or 'q' to quit: ")

                # Handle user canceling
                if startDate.lower() == 'q':
                    print('Input canceled.\n')
                    break
                
                # Remove commas from startDate
                startDate = startDate.replace(',', '')

                # Validate input
                startDate = int(startDate)
                if startDate >= 0:
                    # Update the startDate in the config data
                    config['startDate'] = startDate
                    ConfigurationMenu.write_config(config)
                    break
                else:
                    print('Start date must be greater than or equal to day zero.\n')
            except ValueError:
                print("Start date must be an integer.\n")

    @staticmethod    
    def configure_duration():
        config = ConfigurationMenu.read_config()

        # Configuration information for duration
        print(f"\nConfigure Duration\n==================\nSet the duration of the simulation in days\nCurrent duration: {config.get('duration', 'N/A'):,} {'day' if config.get('duration', 'N/A') == 1 else 'days'}\n")

        while True:
            try:
                # Prompt and store user input
                duration = input("\nEnter the new duration or 'q' to quit: ")

                # Handle user canceling
                if duration.lower() == 'q':
                    print('Input canceled.\n')
                    break
                
                # Remove commas from duration
                duration = duration.replace(',', '')

                # Validate input
                duration = int(duration)
                if duration >= 1:
                    # Update the duration in the config data
                    config['duration'] = duration

                    # Ensure report frequency still works
                    config['reportFrequency'] = ConfigurationMenu.ensure_valid_report_frequency(config, duration)

                    ConfigurationMenu.write_config(config)
                    break
                else:
                    print('Duration must be greater than or equal to one day.\n')
            except ValueError:
                print("Duration must be an integer.\n")

    @staticmethod    
    def configure_report_frequency():
        config = ConfigurationMenu.read_config()

        # Determine the report frequency options based on the duration of the simulation
        duration = config.get('duration', 0)
        options = ConfigurationMenu.get_report_frequency_options(duration)
        formatted_options = ConfigurationMenu.format_options_for_print(options)

        # Configuration information for report frequency
        print(f"\nConfigure Report Frequency\n==========================\nSet the frequency for generating statistic reports\nCurrent report frequency: {config.get('reportFrequency', 'N/A')}\nThe options are {formatted_options}\n")

        while True:
            try:
                # Prompt and store user input
                reportFrequency = input(f"Enter the new report frequency or 'q' to quit: ")

                # Handle user canceling
                if reportFrequency.lower() == 'q':
                    print('Input canceled.\n')
                    break
                
                # Validate input
                reportFrequency = reportFrequency.strip().lower()  # Convert to lowercase and remove leading/trailing spaces
                if reportFrequency in [option for option in options]:
                    # Update the report frequency in the config data
                    config['reportFrequency'] = reportFrequency
                    ConfigurationMenu.write_config(config)
                    break
                else:
                    print(f'Report frequency must be one of the following options: {formatted_options}.\n')
            except ValueError:
                print("Report frequency must be a string.\n")

    def get_report_frequency_options(duration):
        options = ["daily"]

        if duration >= 14:  # 2 weeks
            options.append("weekly")
        if duration >= 61:  # 2 months
            options.append("monthly")
        if duration >= 730:  # 2 years
            options.append("yearly")
        options.append("final")

        return options
    
    def format_options_for_print(options):
        # Add single quotes around each option
        options = [f"'{option}'" for option in options]

        # If there are more than two options, add a comma after each option except for the last two
        if len(options) > 2:
            for i in range(len(options) - 2):
                options[i] += ','
        
        # Add 'or' before the last option
        if len(options) > 2:
            options[-2] += ', or'
        else: 
            options[-2] += ' or'
        # Join the options with spaces
        options = ' '.join(options)

        return options
    
    def ensure_valid_report_frequency(config, duration):
        min_durations = {
            'yearly': 730,
            'monthly': 61,
            'weekly': 14,
            'daily': 2
        }

        for frequency, min_duration in min_durations.items():
            if config['reportFrequency'] == frequency and duration < min_duration:
                return 'final'

    @staticmethod
    def configure_costs():
        cost_options = {
                "Fuel": CostMenu.configure_fuel_cost,
                "Takeoff": CostMenu.configure_takeoff_cost,
                "Landing": CostMenu.configure_landing_cost,
                "Leasing": CostMenu.configure_leasing_costs
            }
        display_menu(cost_options, is_submenu=True)