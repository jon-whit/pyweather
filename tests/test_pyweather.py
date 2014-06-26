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

    def test_something(self):
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

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()