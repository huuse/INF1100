#Cubic_Poly4.py

class Line:

   	def __init__(self, c0, c1):
		self.c0 = c0
		self.c1 = c1
	def __call__(self, x):

		y = self.c0 + self.c1*x
		print 'y = %g for x = %g in a line' %(y,x)
		return y

	def table(self, L, R, n):
		s = ''
		import numpy as np
		for x in np.linspace(L, R, n):
			y = self(x)
			y += '%12g %12g \n' %(x,y)
		return s


class Parabola(Line):
	def __init__(self, c0, c1, c2):
		Line.__init__(self,c0, c1)
		self.c2 = c2

	def __call__(self,x):
		y = self.c2*x**2 + Line.__call__(self, x)
		print 'y = %g for x = %g in a Parabola' %(y,x)
		return y


class Cubic(Parabola):
	def __init__(self, c0, c1, c2, c3):
		Parabola.__init__(self, c0, c1, c2)
		self.c3 = c3

	def __call__(self, x):
		y = self.c3*x**3 + Parabola.__call__(self, x)
		print 'y = %g for x = %g in Poly4' %(y, x)
		return y


class Poly4(Cubic):
	"""docstring for Poly4"""
	def __init__(self, c0, c1, c2, c3, c4):
		Cubic.__init__(self, c0, c1, c2, c3)
		self.c4 = c4

	def __call__(self, x):
		y = self.c4*x**4 + Cubic.__call__(self, x)
		print 'y = %g for x = %g in a Poly4' %(y,x)
		return y


test = Poly4(1, 2, 3, 4, 5)
result = test(x=6)




"""
python Cubic_Poly4.py
y = 13 for x = 6 in a line
y = 121 for x = 6 in a Parabola
y = 985 for x = 6 in Poly4
y = 7465 for x = 6 in a Poly4
"""

		
