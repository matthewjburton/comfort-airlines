"""
Class responsible for implementing simulation config controls.

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = McHale Trotter
"""

import json

class Config:
    """Load config file"""
    def load_config(filename):
        try:
            with open(filename, 'r') as file:
                config = json.load(file)
        except FileNotFoundError:
            # If the file doesn't exist, initialize an empty configuration
            config = {}
        return config

    """Save config file"""
    def save_config(filename, config):
        with open(filename, 'w') as file:
            json.dump(config, file, indent=4)

    """Update config file"""
    def update_config(config, **kwargs):
        if "simulation" not in config:
            config["simulation"] = {}
        config["simulation"].update(kwargs)


# Specify config file (.json)
filename = 'sim_config.json'


# Example usage (load, update, save)

# Load existing configuration or initialize an empty one
# config = Config.load_config(filename)

# Example usage of update_config, (uses kwargs: you can update however many attributes you want at a time)
# Config.update_config(config, cost_fuel=0, cost_gate=0, cost_takeoff=0, cost_landing=0, cost_aircraft=0, start_time_days=0, duration_days=0, report_frequency="daily")

# Save the updated configuration
# Config.save_config(filename, config)
