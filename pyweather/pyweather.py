#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib
import requests
from xml.dom import minidom


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

def yahoo_conditions(zip_code, units='f'):
    """
    Gets the current weather conditions from Yahoo weather. For more information, see https://developer.yahoo.com/weather/.

    :param zip_code: the U.S. zip code for the desired location
    :param units: fahrenheit by default (f). You may also choose celsius by entering c instead of f.
    """

    WEATHER_URL = 'http://weather.yahooapis.com/forecastrss?w=%s&u=%s'
    WEATHER_NS = 'http://xml.weather.yahoo.com/ns/rss/1.0'

    url = WEATHER_URL %(zip_code, units)

    # Try to parse the RSS feed at the given URL.
    try:
        dom = minidom.parse(urllib.request.urlopen(url))
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