"""
Unit testing for the great_cricle.py file

__team_name__ = Cloud Nine
__team_members__ = Jeremy Maas, Matt Burton, McHale Trotter, Kevin Sampson, Justin Chen, Ryan Hirscher
__author__ = Justin Chen

How to use: Execute the following command in the terminal to run the tests:

    python3 test_great_circle.py
    or
    python test_great_circle.py
"""



import unittest
import sys
sys.path.append('../../../')
from unittest.mock import MagicMock
from airport import Airport 
from great_circle import great_circle

class TestGreatCircle(unittest.TestCase):
    def test_same_airport(self):
        # Create a mock airport object for a specific airport (e.g., San Francisco)
        airport_sf = Airport(latitude=37.7749, longitude=-122.4194)

        # Call the great_circle function with the same airport as both arguments
        result_distance = great_circle(airport_sf, airport_sf)

        # Verify that the result is 0
        self.assertEqual(result_distance, 0)

    def test_far_away_airports(self):
        # Create mock airport objects for far-away airports (e.g., San Francisco and New York)
        airport_sf = Airport(latitude=37.7749, longitude=-122.4194)  # San Francisco
        airport_ny = Airport(latitude=40.7128, longitude=-74.0060)   # New York

        # Set up the expected distance between San Francisco and New York
        expected_distance = 2572.08  # miles (approximate)

        # Call the great_circle function
        result_distance = great_circle(airport_sf, airport_ny)

        # Verify that the result is close to the expected distance
        self.assertAlmostEqual(result_distance, expected_distance, places=2)

    def test_close_airports(self):
        # Create mock airport objects for close airports (e.g., two nearby airports in the same city)
        airport_a = Airport(latitude=37.7749, longitude=-122.4194)  # Airport A
        airport_b = Airport(latitude=37.7749, longitude=-122.4194)  # Airport B (close to Airport A)

        # Call the great_circle function
        result_distance = great_circle(airport_a, airport_b)

        # Verify that the result is close to 0
        self.assertAlmostEqual(result_distance, 0, places=2)

if __name__ == '__main__':
    unittest.main()