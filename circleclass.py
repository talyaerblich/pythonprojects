class Circle(object):
	pi = 3.14#global attribute
	def __init__ (self, radius):
		self.radius = radius
	def circumference (self):
		c = 2 * self.pi * self.radius
		return (c)
	def area(self):
		a = self.pi * self.radius ** 2
		return (a)
big_circle = Circle(10)
print(big_circle.circumference())
print(big_circle.area())

	