"""
Class responsible for implementing the menu options under the simulation menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas and Matt Burton
"""
from utilities.display_menu import display_menu
from simulation.simulation import Simulation

import json
import os

class SimulationMenu:

    """Simulation Options"""
    @staticmethod
    def run_simulation():
        print("\nExecuting run_simulation()")
        Simulation.run_simulation()

    @staticmethod
    def configure_simulation():
        print("\nExecuting configure_simulation()")
        configure_options = { 
            "Start date": SimulationMenu.configure_start_date,
            "Duration": SimulationMenu.configure_duration,
            "Report frequency": SimulationMenu.configure_report_frequency,
            "Costs": SimulationMenu.configure_costs,
            "Challenges": SimulationMenu.configure_challenges }
        display_menu(configure_options, is_submenu = True)
    
    @staticmethod
    def analyze_simulation():
        print("\nExecuting analyze_simulation()")
        analyze_options = {
            "Follow aircraft": SimulationMenu.analyze_follow_aircraft,
            "Download report(s)": SimulationMenu.analyze_download_reports
            }
        display_menu(analyze_options, is_submenu=True)



    """Configuration Options"""
    CONFIG_FILE_PATH = 'simulation/simulation_config.json'

    @staticmethod
    def read_config():
        if os.path.exists(SimulationMenu.CONFIG_FILE_PATH):
            with open(SimulationMenu.CONFIG_FILE_PATH, 'r') as f:
                return json.load(f)
        else:
            return {}

    @staticmethod
    def write_config(config_data):
        with open(SimulationMenu.CONFIG_FILE_PATH, 'w') as f:
            json.dump(config_data, f)

    @staticmethod
    def configure_start_date():
        config_data = SimulationMenu.read_config()
        while True:
            try:
                startDate = int(input('Enter the start date (in days): '))
                if 0 <= startDate <= 365:
                    # Update the start date in the config data
                    config_data['startDate'] = startDate
                    SimulationMenu.write_config(config_data)
                    break
                else:
                    print('Start date must be in the range of 0 to 365 days.')
            except ValueError:
                print("Start date must be a number.")

    @staticmethod    
    def configure_duration():
        config_data = SimulationMenu.read_config()
        while True:
            try:
                duration = int(input('Enter the duration (in days): '))
                if 0 <= duration <= 365:
                    # Update the duration in the config data
                    config_data['duration'] = duration
                    SimulationMenu.write_config(config_data)
                    break
                else:
                    print('Duration must be in the range of 0 to 365 days.')
            except ValueError:
                print("Duration must be a number.")

    @staticmethod    
    def configure_report_frequency():
        config_data = SimulationMenu.read_config()

        duration = config_data.get('duration', 0)
        options = ['daily']
        if duration >= 14:  # 2 weeks
            options.append('weekly')
        if duration >= 60:  # 2 months
            options.append('monthly')
        if duration >= 730:  # 2 years
            options.append('yearly')
        options.append('final')

        while True:
            try:
                reportFrequency = str(input(f'Enter the report frequency\n({', '.join(options)}): '))
                if reportFrequency.lower() in options:
                    # Update the report frequency in the config data
                    config_data['reportFrequency'] = reportFrequency.lower()
                    SimulationMenu.write_config(config_data)
                    break
                else:
                    print(f'Report frequency must be either {', '.join(options)}.')
            except ValueError:
                print("Report frequency must be a string.")

    @staticmethod
    def configure_costs():
        print("\nExecuting configure_costs()")
        cost_options = {
                "Fuel": SimulationMenu.configure_fuel_cost,
                "Gate": SimulationMenu.configure_gate_cost,
                "Takeoff": SimulationMenu.configure_takeoff_cost,
                "Landing": SimulationMenu.configure_landing_cost,
                "Aircraft": SimulationMenu.configure_aircraft_cost
            }
        display_menu(cost_options, is_submenu=True)

    @staticmethod    
    def configure_challenges():
        print("\nExecuting configure_challenges()")
        challenge_options = {
                "View": SimulationMenu.view_challenges,
                "Edit": SimulationMenu.edit_challenges 
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



    """Analyze Options"""
    @staticmethod
    def analyze_follow_aircraft():
        print("\nExecuting analyze_follow_aircraft()")

    @staticmethod
    def analyze_download_reports():
        print("\nExecuting analyze_download_reports()")
