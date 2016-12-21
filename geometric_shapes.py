#geometric_shapes.py
import numpy as np
class rectangle:
	def __init__(self, x0, y0, W, H):
		self.x0 = x0
		self.y0 = y0
		self.W = W
		self.H = H


	def area(self):
		return self.W*self.H


	def perimeter(self):
		return self.W*2+self.H*2



	
def test_Rectangle():
	tol = 1e-14
	expect_area = 2*1
	expect_perimeter = 2*2+1*2
	y0=0
	x0=0
	W=2
	H=1
	computed = rectangle(y0, x0, W, H)
	assert abs(expect_area-computed.area())<tol,\
	'bug in rectangle.area, difference = %s' %abs(expect_area-computed.area())
	assert abs(expect_perimeter-computed.perimeter())<tol,\
	'bug in rectangle.perimeter, difference = %s' \
	%abs(expect_perimeter-computed.perimeter())

test_Rectangle()


class triangle:
	def __init__(self, v1, v2, v3):

		self.v1 = v1
		self.v2 = v2
		self.v3 = v3


	def area(self):
		return 0.5*(self.v2[0]*self.v3[1] -self.v3[0]*self.v2[1]-self.v1[0]*self.v3[1]\
			+self.v3[0]*self.v1[1]+self.v1[0]*self.v2[1]\
			-self.v2[0]*self.v1[1])
	


	def perimeter(self):
		
		return np.sqrt((self.v2[0]-self.v1[0])**2+(self.v2[1]-self.v1[1])**2) \
		+np.sqrt((self.v3[0]-self.v2[0])**2+(self.v3[1]-self.v2[1])**2)\
		+np.sqrt((self.v1[0]-self.v3[0])**2+(self.v1[1]-self.v3[1])**2)


def test_Triangle():
	tol = 1e-14
	expect_area = 1*1/2.
	expect_perimeter = 1+1+np.sqrt(2)
	v1 = [0,0]
	v2= [1,0]
	v3 = [0,1]
	computed = triangle(v1, v2, v3)
	assert abs(expect_area-computed.area())<tol,\
	'bug in triangle.area, difference = %s' %abs(expect_area-computed.area())
	assert abs(expect_perimeter-computed.perimeter())<tol,\
	'bug in triangle.perimeter, difference = %s' \
	%abs(expect_perimeter-computed.perimeter())

test_Triangle()


"""
python geometric_shapes.py
"""

