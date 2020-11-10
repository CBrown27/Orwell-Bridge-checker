# Orwell-Bridge-checker

INTRODUCTION
------------

This is a python script that accesses the Twitter API and the OpenWeatherMap API to ascertain whether the Orwell Bridge in Suffolk is closed. It does this by making a GET request specfically for the @HighwaysEAST twitter account, and using the latitiude and longitude of the Orwell Bridge.

REQUIREMENTS
------------

This module requires the following modules (they should be installed alongside python 3.8.0);

- base64 (https://github.com/python/cpython/blob/3.9/Lib/base64.py)
- requests (https://pypi.org/project/requests/)
- operator (https://docs.python.org/3/library/operator.html)

HOW TO USE
-----------

This is very simple to use, simply press the run button to return the results for the Orwell Bridge. If you wish to change the search critera for a differnt location, change the search_params for the TwitterAPI, and change the lat and long values in the OpenWeatherMap url.

FURTHER IMPROVEMENTS
-----------

I plan to further improve this script by accessing a third API, the TomTom traffic API (https://developer.tomtom.com/), to provide traffic updates for the Orwell Bridge.
I also plan to host this script on a website, with a visualised traffic light system to make the information easier to digest

REFERENCES
-----------

https://developer.twitter.com/en/docs/twitter-api
https://openweathermap.org/current
