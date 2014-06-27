#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from urllib.parse import quote
import xml.etree.ElementTree as ET
from pyweather import utils


def noaa_conditions(station_id):
    """
    Gets the current weather conditions from the National Oceanic and Atmospheric Administration's
    (NOAA). For more information, see http://graphical.weather.gov/xml/.

    To find the desired station ID point your browser to http://w1.weather.gov/xml/current_obs/seek.php?state=&Find=Find.
    Then select the state you wish in the -Select a State- drop down box. Click 'Find'. Locate the 4-digit station ID.
    For example, Salt Lake City is identified with the station ID KSLC.

    :param station_id: the unique weather station ID for the desired location (see explanation above).
    """

    base_url = 'http://www.weather.gov/xml/current_obs/%s.xml' % station_id

    # Get the current weather conditions in XML format.
    weather_data = requests.get(base_url)

    return weather_data


def fetch_woeid(location):
    """
    Fetch a location's corresponding WOEID.

    :param location: (string) a location (e.g. 23454 or Salt Lake City, United States)
    :return: a string containing the location's corresponding WOEID or None if the WOEID could not be found.
    :raises:
        :requests.exceptions.RequestException: requests could not open the URL.
        :xml.etree.ElementTree.ParseError: xml.etree.ElementTree failed to parse the XML document.
    """

    woeid_query = ("http://locdrop.query.yahoo.com/v1/public/yql?"
                   "q=select%20woeid%20from%20locdrop.placefinder%20"
                   "where%20text='{0}'")
    url = woeid_query.format(quote(location))

    rss = utils.fetch_xml(url)

    try:
        woeid = rss.find("results/Result/woeid").text
    except AttributeError:
        return None

    return woeid


def yahoo_conditions(location, units='f'):
    """
    Gets the current weather conditions from Yahoo weather. For more information, see https://developer.yahoo.com/weather/.

    :param location: a location (e.g. Salt Lake City, United States)
    :param units: fahrenheit by default (f). You may also choose celsius by entering c instead of f.
    """

    weather_url = 'http://weather.yahooapis.com/forecastrss?w=%s&u=%s'
    weather_ns = 'http://xml.weather.yahoo.com/ns/rss/1.0'
    woeid = fetch_woeid(location)

    url = weather_url % (woeid, units)

    # Try to parse the RSS feed at the given URL.
    try:
        rss = ET.parse(requests.get(url, stream=True).raw).getroot()

        conditions = rss.find('channel/item/{%s}condition' % weather_ns)

        return {
            'current_condition': conditions.get('text'),
            'current_temp': conditions.get('temp'),
            'title': rss.findtext('channel/title')
        }
    except:
        raise


def openweather_conditions(city_name, units='imperial', lang='en'):
    """
    Gets the current weather conditions (in JSON format) from the Open Weather Map service. For more information, see
    http://openweathermap.org/.

    :param city_name: the name of the city and its state in 'city, state' format
    :param units: the desired units of measurement
    :param lang: the language the data is returned with
    """

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Generate the data for the request.
    payload = {'q':city_name, 'units':units, 'lang':lang}

    try:
        # Attempt to get the data from the Open Weather API.
        request = requests.get(base_url, params=payload)
    except:
        raise

    weather_data = request.json()

    return weather_data