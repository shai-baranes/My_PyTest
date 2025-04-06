import math

class Shape:
	"""docstring for Shape"""

	def area(self):
		pass

	def perimeter(self):
		pass



class Circle(Shape):
	"""docstring for Circle"""
	def __init__(self, radius):
		self.radius = radius

	def area(self):
		return math.pi * self.radius ** 2

	def perimeter(self):
		return 2 * math.pi * self.radius
		


class Rectangle(Shape):
	"""docstring for Rectangle"""
	def __init__(self, length, width):
		self.length = length
		self.width = width


	def __eq__(self, other):
		if not isinstance(other, Rectangle):
			return False
		return self.width == other.width and self.length == other.length



	def area(self):
		return self.length * self.width

	def perimeter(self):
		return 2 * self.length + 2 * self.width



class Square(Rectangle):
	"""docstring for Square"""
	def __init__(self, length):
		super().__init__(length, length)
		# super(Square, self).__init__(length, length) # works the same as above (taken from auto-generated template)


