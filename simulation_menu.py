"""
Class responsible for implementing the menu options under the simulation menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas and Matt Burton
"""
from menu import display_menu
class SimulationMenu:

    """SimulationOptions"""

    @staticmethod
    def run_simulation():
        print("\nExecuting run_simulation()")

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
    def follow_aircraft():
        print("\nExecuting follow_aircraft()")

    @staticmethod
    def download_reports():
        print("\nExecuting download_reports()")

    @staticmethod
    def configure_start_date():
        print("\nExecuting configure_start_date()")

    @staticmethod    
    def configure_duration():
        print("\nExecuting configure_duration()")

    @staticmethod    
    def configure_report_frequency():
        print("\nExecuting configure_report_frequency()")

    @staticmethod
    def configure_costs():
        print("\nExecuting configure_costs()")
        cost_options = {
                "Fuel": None,
                "Gate": None,
                "Takeoff": None,
                "Landing": None,
                "Aircraft": None
            }
        display_menu(cost_options, is_submenu=True)

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

    @staticmethod    
    def configure_challenges():
        print("\nExecuting configure_challenges()")
        challenge_options = {
                "View": SimulationMenu.view_challenges,
                "Edit": SimulationMenu.edit_challenges 
                }
        display_menu(challenge_options, is_submenu=True)

    @staticmethod
    def view_challenges():
        print("\nExecuting view_challenges()")

    @staticmethod
    def edit_challenges():
        print("\nExecuting edit_challenges()")

    @staticmethod
    def analyze_simulation():
        print("\nExecuting analyze_simulation()")
        analyze_options = {
            "Follow aircraft": SimulationMenu.analyze_follow_aircraft,
            "Download report(s)": SimulationMenu.analyze_download_reports
            }
        display_menu(analyze_options, is_submenu=True)

    @staticmethod
    def analyze_follow_aircraft():
        print("\nExecuting analyze_follow_aircraft()")

    @staticmethod
    def analyze_download_reports():
        print("\nExecuting analyze_download_reports()")
