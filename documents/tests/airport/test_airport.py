"""
Unit testing for the airport.py file

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Matt Burton

How to use: Execute the following command in the terminal to run the tests:

    python3 test_airport.py
"""
import unittest
from unittest.mock import patch
import sys
sys.path.append('../../../') # provide access to modules in the comfort-airlines directory
from airport import Airport

class TestAirport(unittest.TestCase):

    def setUp(self):
        # Create a mock airport object for testing
        self.mock_airport = Airport(1,'John F. Kennedy International Airport', 'JFK', 40.641766, -73.780968, -5, 19034000, 5, 3, 0)

    """Test each of the the methods in airport.py"""

    def test_get_airport_id(self):
        self.assertEqual(self.mock_airport.get_airport_id(), 1)

    def test_get_airport_name(self):
        self.assertEqual(self.mock_airport.get_airport_name(), "John F. Kennedy International Airport")

    def test_get_airport_abbreviation(self):
        self.assertEqual(self.mock_airport.get_airport_abbreviation(), "JFK")

    def test_get_airport_latitude(self):
        self.assertEqual(self.mock_airport.get_airport_latitude(), 40.641766)

    def test_get_airport_longitude(self):
        self.assertEqual(self.mock_airport.get_airport_longitude(), -73.780968)

    def test_get_airport_timezone_offset(self):
        self.assertEqual(self.mock_airport.get_airport_timezone_offset(), -5)

    def test_get_metro_population(self):
        self.assertEqual(self.mock_airport.get_metro_population(), 19034000)

    def test_get_total_gates(self):
        self.assertEqual(self.mock_airport.get_total_gates(), 5)

    def test_get_available_gates(self):
        self.assertEqual(self.mock_airport.get_available_gates(), 3)

    def test_get_is_hub(self):
        self.assertFalse(self.mock_airport.get_is_hub())

    def test_remove_gate(self):
        self.mock_airport.remove_gate()
        self.assertEqual(self.mock_airport.get_available_gates(), 2)

    def test_add_gate(self):
        self.mock_airport.add_gate()
        self.assertEqual(self.mock_airport.get_available_gates(), 4)

if __name__ == '__main__':
    unittest.main()
