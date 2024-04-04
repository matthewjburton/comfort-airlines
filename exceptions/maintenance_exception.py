"""
Handles error looging for invalid maintenance calls

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

class MaintenanceError(Exception):
    """Exception raised for maintenance-related errors."""

    def __init__(self, message):
        self.message = "Maintenance Error: " + message
        super().__init__(self.message)