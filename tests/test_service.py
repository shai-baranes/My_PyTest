
import os, sys
# script_path = os.path.realpath(os.path.dirname(__name__))
# os.chdir(script_path)
# sys.path.append("..")

import pytest
import unittest.mock as mock
import src.service as service
import requests


#mock while using the unittest package
@mock.patch("src.service.get_user_from_db")
def test_get_user_from_db(mock_get_user_from_db):     
	mock_get_user_from_db.return_value = "Mocked Alice"
	user_name1 = service.get_user_from_db(1) # here we apply the actual call (as if penetrates the entire flow)
	user_name2 = service.get_user_from_db(2) # no matter the param, the return is always "Mocked Alice" as defined above

	assert  user_name1 == "Mocked Alice"
	assert  user_name2 == "Mocked Alice"

	# the true intention is to be able to inject a plausable result whenever there's  af cuntion call and we can tag such that running only when no connectivity (w/ valid outcomes)




def test_get_users(mocker):
	# mock requests.get
	mock_get = mocker.patch("requests.get") # from the MockWeather.py file

	# Set / mock return values
	mock_get.return_value.status_code = 200
	mock_get.return_value.json.return_value = {"id": 1, "name": "John Doe"}

	# Call function
	result = service.get_users()

	#Assertions
	assert result == {"id": 1, "name": "John Doe"}
	mock_get.assert_called_once_with("https://jsonplaceholder.typicode.com/users") # here to verify that 'MockWeather.requests.get' was called (mock assert has all king of potential testing)



def test_get_users_error(mocker):
	# mock requests.get
	mock_get = mocker.patch("requests.get") # from the MockWeather.py file

	# Set / mock return values
	mock_get.return_value.status_code = 400 # expecting error here
	with pytest.raises(requests.HTTPError):
		service.get_users()
