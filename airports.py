# Purpose:    Pull Airport information from our database into a Python class
#             allowing for easier access of information.
#             Also adds get methods to gather specific airport information.
#
# Authors:    Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
#
# How to use: Import airports.py in file, and create Airports class object.
#             Run methods as part of Airports class object.
#
# Example:    import airports
#             test_obj = Airports()
#             ishub = test_obj.is_hub("JFK") // Will set ishub to false


import mysql.connector
import pandas as pd


class Airports:

    def __init__(self):

        # Establish Database connection
        db_connection = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="Cloud9",
            database="cloudnine"
        )

        # Run base query to gather all information from airports table
        query = pd.read_sql_query('''SELECT * FROM airports''', db_connection)

        # Put query results into a Pandas dataframe
        self.dataframe = pd.DataFrame(query, columns=['airport_id', 'name', 'abbreviation', 'latitude', 'longitude',
                                                 'timezone_offset', 'metro_population', 'total_gates', 'is_hub'])

        # Format dataframe to remove 'b' strings using utf-8 format
        self.dataframe['is_hub'] = self.dataframe['is_hub'].str.decode('utf-8')

    # Function to grab all information about an airport given an abbreviation
    # Puts information into a dictionary object
    #
    # Note: to_dict function cannot set each column equal to a single value
    #       Closest workaround is to set each column equal to a list of 1.
    #       Then we change the key's values from a list of 1 to the single value in that list of 1
    def get_airport_info(self, abbreviation):
        airport = self.dataframe.loc[self.dataframe['abbreviation']== abbreviation].to_dict(orient='list')
        for x in airport:
           airport[x] = airport[x][0]
        return airport

    # Below: Individual get functions, takes indidivual airport abbreviation 
    #        and returns associated value

    def get_airport_id(self, abbreviation):
        return self.get_airport_info(abbreviation)['airport_id']

    def get_airport_name(self, abbreviation):
        return self.get_airport_info(abbreviation)['name']

    def get_airport_latitude(self,abbreviation):
        return self.get_airport_info(abbreviation)['latitude']

    def get_airport_longitude(self, abbreviation):
        return self.get_airport_info(abbreviation)['longitude']

    def get_airport_timezone_offset(self, abbreviation):
        return self.get_airport_info(abbreviation)['timezone_offset'] 

    def get_metro_population(self, abbreviation):
        return self.get_airport_info(abbreviation)['metro_population']

    def get_total_gates(self, abbreviation):
        return self.get_airport_info(abbreviation)['total_gates']

    def is_hub(self, abbreviation):
        if(self.get_airport_info(abbreviation)['is_hub'] == '0'):
            return False
        return True    