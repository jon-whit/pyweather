#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
from pyweather import utils


def yahoo_conditions(location, units='f'):
    """
    Gets the current weather conditions from Yahoo weather. For more information, see
    https://developer.yahoo.com/weather/.

    :param location: a location in 'city, state, country' format (e.g. Salt Lake City, Utah, United States)
    :param units: fahrenheit by default (f). You may also choose celsius by entering c instead of f.
    :return: The current weather conditions for the given location. None if the location is invalid.
    """

    weather_url = 'http://weather.yahooapis.com/forecastrss?w=%s&u=%s'
    weather_ns = 'http://xml.weather.yahoo.com/ns/rss/1.0'
    woeid = utils.fetch_woeid(location)

    if woeid is None:
        return None

    url = weather_url % (woeid, units)

    # Try to parse the RSS feed at the given URL.
    try:
        rss = utils.fetch_xml(url)
        conditions = rss.find('channel/item/{%s}condition' % weather_ns)

        return {
            'title': rss.findtext('channel/title'),
            'current_condition': conditions.get('text'),
            'current_temp': conditions.get('temp'),
            'date': conditions.get('date'),
            'code': conditions.get('code')
        }
    except:
        raise


def openweather_conditions(location, units='imperial', lang='en'):
    """
    Gets the current weather conditions (in JSON format) from the Open Weather Map service. For more information, see
    http://openweathermap.org/current.

    :param location: a location in 'city, state, country' format (e.g. Salt Lake City, Utah, United States)
    :param units: the desired units of measurement (imperial or metric)
    :param lang: the language the data is returned with
    :return The current weather conditions for the given location. None if the location is invalid.
    """

    base_url = 'http://api.openweathermap.org/data/2.5/weather'

    # Generate the data for the request.
    payload = {'q':location, 'units':units, 'lang':lang}

    try:
        # Attempt to get the data from the Open Weather API.
        request = requests.get(base_url, params=payload)
    except:
        raise

    weather_data = request.json()

    if weather_data['cod'] == "404":
        return None

    return weather_data