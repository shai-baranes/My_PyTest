import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")


import pytest
from src.is_prime import is_prime



# #don't forget to add the "test_" initials before each method that behaves as a veification point!
# def test_prime_numbers_check():
# 	assert is_prime(1) == False
# 	assert is_prime(2) == True
# 	assert is_prime(3) == True
# 	assert is_prime(4) == False
# 	assert is_prime(5) == True
# 	assert is_prime(15) == False
# 	assert is_prime(17) == True
# 	assert is_prime(18) == False
# 	assert is_prime(19) == True
# 	assert is_prime(25) == False




#### another option:
@pytest.mark.parametrize("num, expected", [
	(1, False),
	(2, True),
	(3, True),
	(4, False),
	(5, True),
	(15, False),
	(17, True),
	(18, False),
	(19, True),
	(25, False),
])

def test_is_prime(num, expected):
	assert is_prime(num) == expected