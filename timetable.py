"""
Implements the funcitonality of the user options from the Timetable section of the main menu

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton
"""

import database

class Timetable:
    def view_timetable():
        # Query the database for the routes table
        db = database.Database()
        query = 'SELECT * FROM routes'
        dataframe = db.execute_query_to_dataframe(query)

        # Print the time table
        print(dataframe)
        