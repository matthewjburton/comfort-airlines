import unittest
from unittest.mock import patch
import sys
sys.path.append('../../../')
from database import Database

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database()

    @patch('database.mysql.connector.connect')
    def test_connect(self, mock_connect):
        self.db.connect()
        mock_connect.assert_called_once()

    @patch('database.mysql.connector.connect')
    def test_disconnect(self, mock_connect):
        self.db.connect()
        self.db.disconnect()
        self.assertIsNone(self.db.connection)

    @patch('database.mysql.connector.connect')
    def test_execute_query(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [(1, 'Airport1'), (2, 'Airport2')]
        result = self.db.execute_query('SELECT * FROM airports')
        self.assertIsNotNone(result)

    @patch('database.mysql.connector.connect')
    def test_execute_query_to_dataframe(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.description = [('id',), ('name',)]
        mock_cursor.fetchall.return_value = [(1, 'Airport1'), (2, 'Airport2')]
        df = self.db.execute_query_to_dataframe('SELECT * FROM airports')
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 2)
        self.assertListEqual(list(df.columns), ['id', 'name'])

    @patch('database.mysql.connector.connect')
    def test_execute_insert_update_delete_query(self, mock_connect):
        """INSERT"""
        insert_query = """
        INSERT INTO airports (name, abbreviation, latitude, longitude, timezone_offset, metro_population, is_hub)
        VALUES ('Test Airport', 'TST', 0.0, 0.0, 0, 10000, 0)
        """
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = []
        self.db.execute_query(insert_query)

        """UPDATE"""
        update_query = """
        UPDATE airports
        SET name = 'Updated Test Airport'
        WHERE abbreviation = 'JFK'
        """
        self.db.execute_query(update_query)

        """DELETE"""
        delete_query = """
        DELETE FROM airports
        WHERE abbreviation = 'JFK'
        """
        self.db.execute_query(delete_query)

if __name__ == '__main__':
    unittest.main()
