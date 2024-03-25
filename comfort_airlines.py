"""
The main executable program for the user interface. 
Responsible for displaying the features and options menus and calling the corresponding methods.

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""
from menu import display_menu
from timetable_menu import TimetableMenu
from simulation_menu import SimulationMenu
from airport_menu import AirportMenu
from aircraft_menu import AircraftMenu

menu_options = {
    "Timetable": {
        "View": TimetableMenu.view_timetable,
        "Search routes": TimetableMenu.search_routes,
        "Edit": TimetableMenu.edit_timetable,
        "Download": TimetableMenu.download_timetable,
    },
    "Simulation": {
        "Run": SimulationMenu.run_simulation,
        "Configure": SimulationMenu.configure_simulation,
        "Analyze": SimulationMenu.analyze_simulation
    },
    "Airports": {
        "View": AirportMenu.view_airport,
        "Edit": AirportMenu.edit_airport
    },
    "Aircraft": {
        "View": AircraftMenu.view_aircraft,
        "Edit": AircraftMenu.edit_aircraft
    },
}

def main():
    display_menu(menu_options)

if __name__ == "__main__":
    main()
