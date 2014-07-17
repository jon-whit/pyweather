#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_utils
----------------------------------

Tests for `utils` module.
"""

import unittest
from pyweather import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        pass

    def test_fetch_xml1(self):

        url = 'http://weather.yahooapis.com/forecastrss?w=2502265'
        rss = utils.fetch_xml(url)

        expected_root = 'rss'
        actual_root = rss.tag
        self.assertEqual(expected_root, actual_root)

        weather_ns = 'http://xml.weather.yahoo.com/ns/rss/1.0'
        location_tag = '{%s}location' % weather_ns
        units_tag = '{%s}units' % weather_ns
        wind_tag = '{%s}wind' % weather_ns
        atmosphere_tag = '{%s}atmosphere' % weather_ns
        astronomy_tag = '{%s}astronomy' % weather_ns
        expected_tags = ['title', 'link', 'description', 'language', 'lastBuildDate', 'ttl', location_tag,
                         units_tag, wind_tag, atmosphere_tag, astronomy_tag]

        valid_xml = True
        for tag in expected_tags:
            element = rss.find('channel/%s' %tag)

            if element is None:
                valid_xml = False

        self.assertTrue(valid_xml)

    def test_fetch_woeid1(self):
        """
        Lookup the WOEID for various locations and assert they are all correct based on Ross Elliot's WOEID lookup. For
        more information, see http://woeid.rosselliot.co.nz/
        """

        # Test Salt Lake City
        location1 = "Salt Lake City, UT, United States"
        expected_woeid1 = "2487610"
        actual_woeid1 = utils.fetch_woeid(location1)
        self.assertEqual(expected_woeid1, actual_woeid1)

        # Test San Francisco
        location2 = "San Francisco, CA, United States"
        expected_woeid2 = "2487956"
        actual_woeid2 = utils.fetch_woeid(location2)
        self.assertEqual(expected_woeid2, actual_woeid2)

        # Test New York City
        location3 = "New York City, NY, United States"
        expected_woeid3 = "2459115"
        actual_woeid3 = utils.fetch_woeid(location3)
        self.assertEqual(expected_woeid3, actual_woeid3)

    def test_fetch_woeid2(self):
        """
        Lookup the WOEID for an unknown location.
        """

        location = "unknown_location"
        expected_woeid = None
        actual_woeid = utils.fetch_woeid(location)
        self.assertEqual(expected_woeid, actual_woeid)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()
