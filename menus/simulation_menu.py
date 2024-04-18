"""
Responsible for implementing the menu options under the simulation menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas and Matt Burton
"""
from utilities.display_menu import display_menu
from simulation.simulation import Simulation
from .configuration_menu import ConfigurationMenu

class SimulationMenu:
    """Simulation Options"""

    @staticmethod
    def run_simulation():
        """
        Runs the simulation.
        """
        Simulation.run_simulation()

    @staticmethod
    def configure_simulation():
        """
        Displays the menu for configuring simulation options.
        """
        configure_options = { 
            "Start date": ConfigurationMenu.configure_start_date,
            "Duration": ConfigurationMenu.configure_duration,
            "Report frequency": ConfigurationMenu.configure_report_frequency,
            "Costs": ConfigurationMenu.configure_costs,
            }
        display_menu(configure_options, is_submenu = True)
    
    @staticmethod
    def analyze_simulation():
        """
        Executes the analyze simulation submenu.
        """
        print("\nExecuting analyze_simulation()")
        analyze_options = {
            "Follow aircraft": SimulationMenu.analyze_follow_aircraft,
            "Download report(s)": SimulationMenu.analyze_download_reports
            }
        display_menu(analyze_options, is_submenu=True)


    """Analyze Options"""
    @staticmethod
    def analyze_follow_aircraft():
        """
        Executes the follow aircraft analysis option.
        """
        print("\nExecuting analyze_follow_aircraft()")

    @staticmethod
    def analyze_download_reports():
        """
        Executes the download reports analysis option.
        """
        print("\nExecuting analyze_download_reports()")
