#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_pyweather
----------------------------------

Tests for `pyweather` module.
"""

import unittest
from pyweather import pyweather


class TestPyweather(unittest.TestCase):

    def setUp(self):
        pass

    def test_openweather_conditions1(self):
        """
        Get the weather conditions for 'Salt Lake City, Utah' and verify that the returned object contains the properties:

        id
        dt
        coord.lat coord.lng
        name
        main.temp
        main.humidity
        main.pressure
        wind.speed
        wind.deg
        clouds.all

        For more information, see the Weather Parameters page http://openweathermap.org/weather-data.
        """

        city_name = 'Salt Lake City, Utah'
        conditions = pyweather.openweather_conditions(city_name)

        expected_keys = ['id', 'dt', 'coord', 'name', 'main', 'wind', 'clouds']
        actual_keys = conditions.keys()

        outcome = all(k in actual_keys for k in expected_keys)
        self.assertTrue(outcome)

    def test_openweather_conditions2(self):
        """
        Attempt to get the weather conditions for an unknown city. As per the API a JSON object will be returned like so:
        {"message":"Error: Not found city","cod":"404"}
        """

        city_name = 'badcity'
        conditions = pyweather.openweather_conditions(city_name)

        expected_keys = ['id', 'dt', 'coord', 'name', 'main', 'wind', 'clouds']
        actual_keys = conditions.keys()

        outcome = all(k in actual_keys for k in expected_keys)
        self.assertFalse(outcome)

        message = "Error: Not found city"
        cod = "404"
        self.assertEqual(conditions.get('message'), message)
        self.assertEqual(conditions.get('cod'), cod)

    def test_fetch_woeid1(self):
        """
        Lookup the WOEID for various locations and assert they are all correct based on Ross Elliot's WOEID lookup. For
        more information, see http://woeid.rosselliot.co.nz/
        """

        # Test Salt Lake City
        location1 = "Salt Lake City, UT, United States"
        expected_woeid1 = "2487610"
        actual_woeid1 = pyweather.fetch_woeid(location1)
        self.assertEqual(expected_woeid1, actual_woeid1)

        # Test San Francisco
        location2 = "San Francisco, CA, United States"
        expected_woeid2 = "2487956"
        actual_woeid2 = pyweather.fetch_woeid(location2)
        self.assertEqual(expected_woeid2, actual_woeid2)

        # Test New York City
        location3 = "New York City, NY, United States"
        expected_woeid3 = "2459115"
        actual_woeid3 = pyweather.fetch_woeid(location3)
        self.assertEqual(expected_woeid3, actual_woeid3)

    def test_fetch_woeid2(self):
        """
        Lookup the WOEID for an unknown location.
        """

        location = "badcity"
        expected_woeid = None
        actual_woeid = pyweather.fetch_woeid(location)
        self.assertEqual(expected_woeid, actual_woeid)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()