"""
API for interfacing with the database

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Example usage:
    import database

    db = Database()
    query = 'SELECT * FROM airports'
    result_df = db.execute_query_to_dataframe(query, params)
"""

import mysql.connector
import pandas as pd

class Database:
    """Constructor"""
    def __init__(self):
        # Initialize database credentials
        self.host = "localhost"
        self.user = 'admin'
        self.password = 'Cloud9'
        self.database = 'cloudnine'
        self.connection = None
        self.cursor = None
        
    """Establishes a connection to the database."""
    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to the database: {e}")

    """Closes the database connection."""
    def disconnect(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    """Executes the given SQL query."""
    def execute_query(self, query, params=None):
        try:
            if not self.connection:
                self.connect()
            self.cursor.execute(query, params)
            return self.cursor
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    """Executes the given SQL query and returns results as a pandas DataFrame."""
    def execute_query_to_dataframe(self, query, params=None):
        try:
            if not self.connection:
                self.connect()
            cursor = self.execute_query(query, params)
            data = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            dataframe = pd.DataFrame(data, columns=columns)

            return dataframe
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    """Executes INSERT, UPDATE, or DELETE SQL query."""
    def execute_insert_update_delete_query(self, query, params=None):
        try:
            if not self.connection:
                self.connect()
            self.execute_query(query, params)
            self.connection.commit()
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")