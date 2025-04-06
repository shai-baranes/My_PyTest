import os, sys, time
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

import pytest
import src.shapes_inheritance as shapes
import math
from pytest_dependency import depends


# instead of fixtures we can utilize test class to adopt both setup & teardown methods (similar to what we've done w/ the before and after yield function)
# test dependencies work here as well :)

class TestCircle: # also the class must gave the "Test" prefix
	"""docstring for ClassName"""
	def setup_method(self, method): # note that 'setup_method' & 'teardown_method' are reserved and it works only using these names! ('method' is each of the following test methods)
		print(f"\nSetting up {method}")
		self.circle = shapes.Circle(10)

	def teardown_method(self, method):
		print(f"\nTearing down {method}")


	@pytest.mark.dependency(name="test_one")
	def test_one(self):
		assert True

	@pytest.mark.dependency(depends=["test_one"]) # can have a list of TCs here
	def test_two(self):
		assert True

	def test_radius(self):
		assert self.circle.radius == 10

	def test_area(self):
		assert self.circle.area() == math.pi * self.circle.radius ** 2

	def test_perimeter(self):
		result = self.circle.perimeter()
		expected = 2 * math.pi * self.circle.radius
		assert result == expected


	def test_area_not_same_circle_rectangle(self, my_rectangle): # to use 'my_rectangle' global for multiple tests
		assert self.circle.area() != my_rectangle.area()