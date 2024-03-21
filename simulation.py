"""
Class responsible for implementing the menu options under the simulation menu option

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Jeremy Maas
"""

class SimulationMenu:

    """SimulationOptions"""

    @staticmethod
    def run_simulation():
        print("\nExecuting run_simulation()")

    #configure_simulation function can maybe be split up, open to discuss
    @staticmethod
    def configure_simulation(startDate, duration, reportFrequency, costs, challenges): #maybe make costs an object that contains information
        print("\nExecuting configure_simulation()")

    @staticmethod
    def view_challenges():#Called within configure_simulation
        print("\nExecuting view_challenges()")

    @staticmethod
    def edit_challenges(): #Would return challenges to configure_simulation function
        print("\nExecuting edit_challenges()")

    @staticmethod
    def follow_aircraft():
        print("\nExecuting follow_aircraft()")

    @staticmethod
    def download_reports(reportFrequency):
        print("\nExecuting download_reports()")
