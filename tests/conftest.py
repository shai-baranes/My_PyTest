import os, sys, time
script_path = os.path.realpath(os.path.dirname(__name__))
os.chdir(script_path)
sys.path.append("..")


import pytest
import src.shapes_inheritance as shapes

@pytest.fixture
def my_rectangle():
	return shapes.Rectangle(10,20)


@pytest.fixture
def other_rectangle():
	return shapes.Rectangle(5, 6)


@pytest.fixture
def my_Square():
	return shapes.Square(5)

