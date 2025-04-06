

## fixtures are moved into the conftest.py file (as well as the other imports)
# @pytest.fixture
# def my_rectangle():
# 	return shapes.Rectangle(10,20)


# @pytest.fixture
# def other_rectangle():
# 	return shapes.Rectangle(5, 6)




def test_rect_area(my_rectangle): # my_rectangle (and other_rectangle) are defined in the testconf.py file
	# rectangle = shapes.Rectangle(10,20)
	assert my_rectangle.area() == 200


def test_rect_permeter(my_rectangle):
	# rectangle = shapes.Rectangle(10,20)
	assert my_rectangle.perimeter() == 60


def test_rect_not_equal(my_rectangle, other_rectangle):
	assert my_rectangle != other_rectangle


