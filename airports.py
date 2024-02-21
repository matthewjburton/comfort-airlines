# Purpose:  Pull Airport information from our database into a Python class, allowing for easier access of information
#
# Author:   Jeremy Maas

import mysql.connector
import pandas as pd


class Airports:

    def __init__(self):
        db_connection = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="Cloud9",
            database="cloudnine"
        )
        query = pd.read_sql_query('''SELECT * FROM Airports''', db_connection)
        dataframe = pd.DataFrame(query, columns=['airport_id', 'name', 'abbreviation', 'latitude', 'longitude',
                                                 'timezone_offset', 'metro_population', 'total_gates', 'is_hub'])
        print(dataframe)


airports_objects = Airports()
