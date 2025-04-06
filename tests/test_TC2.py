import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

import pytest 
from src.TC2 import get_weather


def test_get_weather():
	assert get_weather(20) == "cold"
	assert get_weather(21) == "hot"




@pytest.mark.skip # w/ there's also optional condition support for 'skipif'
def test_get_weather_skipped():
	assert get_weather(5) == "cold"
	assert get_weather(30) == "hot"

