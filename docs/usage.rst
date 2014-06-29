========
Usage
========

To use pyweather in a project::

	import pyweather


-------------------------
OpenWeatherMap Conditions
-------------------------

To get the current weather conditions from the OpenWeatherMap service::

    pyweather.openweather_conditions(location)

The location must be given in 'City, State, Country' format to ensure you get the desired location. Otherwise the OpenWeatherMap
API will interpret the location as it pleases. For unique city name, only the city is needed. However, it is best to ensure
as much accuracy as possible by providing the state and country.

For example, to get the current weather conditions for Salt Lake City, Utah, United States::

    location = 'Salt Lake City, Utah, United States'
    conditions = pyweather.openweather_conditions(location)
    current_temp = conditions['main']['temp']
    current_humidity = conditions['main']['humidity']
    current_pressure = conditions['main']['pressure']

For a better list of the properties available, please refer to the API.

------------------------
Yahoo Weather Conditions
------------------------

To get the current weather conditions from Yahoo's weather service:

    pyweather.yahoo_conditions(location)

For example, to get the current weather conditions for New York City, New York, United States::

    location = 'New York City, New York, United States'
    conditions = pyweather.yahoo_conditions(location)
    current_condition = conditions['current_condition']
    current_temp = conditions['current_temp']
    current_date = conditions['date']
    weather_code = conditions['code']


