import os, sys
# script_path = os.path.realpath(os.path.dirname(__name__))
# os.chdir(script_path)
# sys.path.append("..")

import pytest 
from src.TC3 import UserManager



@pytest.fixture
def user_manager():
	"""Creates a fresh instanch of UserManager before each test."""
	return UserManager()



def test_add_user(user_manager):
	assert user_manager.add_user("john_doe", "john@example.com") == True
	assert user_manager.get_user("john_doe") == "john@example.com", "mail should be: john@example.com"
	# assert user_manager.get_user("john_doe") == "john_@example.com"

def test_add_duplicate_user(user_manager):
	user_manager.add_user("john_doe", "john@example.com")
	with pytest.raises(ValueError):
		user_manager.add_user("john_doe", "another@example.com")





# -----------------------
# you can also do it without the fixute bug the depndency between tests shall results w/ a failure
# -----------------------


# user_manager = UserManager()



# def test_add_user():
# 	assert user_manager.add_user("john_doe", "john@example.com") == True
# 	assert user_manager.get_user("john_doe") == "john@example.com", "mail should be: john@example.com"
# 	# assert user_manager.get_user("john_doe") == "john_@example.com"

# def test_add_duplicate_user():
# 	user_manager.add_user("john_doe", "john@example.com")
# 	with pytest.raises(ValueError):
# 		user_manager.add_user("john_doe", "another@example.com")


