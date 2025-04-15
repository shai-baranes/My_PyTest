import os, sys
# script_path = os.path.realpath(os.path.dirname(__name__))
# os.chdir(script_path)
# sys.path.append("..")

import pytest
from src.MockWeather import get_weather

def test_get_weather(mocker):
	# mock requests.get
	mock_get = mocker.patch("src.MockWeather.requests.get") # from the MockWeather.py file

	# Set / mock return values
	mock_get.return_value.status_code = 200
	mock_get.return_value.json.return_value = {"temperature": 25, "condition": "Sunny"}

	# Call function
	result = get_weather("Dubai")

	#Assertions
	assert result == {"temperature": 25, "condition": "Sunny"}
	mock_get.assert_called_once_with("https://api.weather.com/v1/Dubai") # here to verify that 'MockWeather.requests.get' was called (mock assert has all king of potential testing)
