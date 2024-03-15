"""
API for interfacing with the database

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

Example usage:
    import database

    db = Database()
    query = 'SELECT * FROM airports'
    result_df = db.execute_query_to_dataframe(query)
"""

import mysql.connector
import pandas as pd
import os
from dotenv import load_dotenv

class Database:
    """Constructor"""
    def __init__(self):
        # Specify the path to the .env file
        dotenv_path = "./docker/.env"

        # Load variables from the specified .env file
        load_dotenv(dotenv_path)

        # Initialize database credentials
        self.host = "localhost"
        self.user = os.environ.get("DB_USER")
        self.password = os.environ.get("DB_PASS")
        self.database = os.environ.get("DB_NAME")
        self.connection = None
        
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
    def execute_query(self, query):
        try:
            if not self.connection:
                self.connect()
            self.cursor.execute(query)
            return self.cursor
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    """Executes the given SQL query and returns results as a pandas DataFrame."""
    def execute_query_to_dataframe(self, query):
        try:
            if not self.connection:
                self.connect()
            cursor = self.execute_query(query)
            data = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            return pd.DataFrame(data, columns=columns)
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")

    """Executes INSERT, UPDATE, or DELETE SQL query."""
    def execute_insert_update_delete_query(self, query):
        try:
            if not self.connection:
                self.connect()
            self.execute_query(query)
            self.connection.commit()
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error executing query: {e}")