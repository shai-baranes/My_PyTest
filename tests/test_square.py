import os, sys
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")

import pytest
import src.shapes_inheritance as shapes

def test_square_area_1(my_Square):
	assert my_Square.area() == 25


def test_square_area_2(my_Square):
	assert my_Square.area() == my_Square.length ** 2



@pytest.mark.parametrize("length, result", [
	(2, 8),
	(5, 20),
	(20, 80),
])



def test_multiple_squares_perimeter(length, result):
	assert shapes.Square(length).perimeter() == result