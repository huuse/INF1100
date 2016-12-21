#circle_test.py

class Circle:
    def __init__(self, x0, y0, R):
	self.x0, self.y0, self.R = x0, y0, R
	def area(self):
    	return pi*self.R**2
	def circumference(self):
    	return 2*pi*self.R

c = Circle(2, -1, 5)

print c.x0