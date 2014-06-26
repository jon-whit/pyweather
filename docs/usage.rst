========
Usage
========

To use pyweather in a project::

	import pyweather


-------------------------
OpenWeatherMap Conditions
-------------------------

To get the current weather conditions from the OpenWeatherMap service::

    pyweather.openweather_conditions(city_name)

For example, to get the current weather conditions for Salt Lake City, Utah::

    city_name = 'Salt Lake City, Utah'
    pyweather.openweather_conditions(city_name)

The city name must be given in 'City, State' format to ensure you get the desired location. Otherwise the OpenWeatherMap
API will interpret the location as it pleases.
