#Quadratic.py

import numpy as np
import cmath as cm

from numpy.lib.scimath import *
class Quadratic:	
	def __init__(self, a, b, c):
		"""
		takes a,b,c from the quadratic formula
		and make them available for the methods
		"""
		self.a = a
		self.b = b 
		self.c = c 

	def value(self,x):
		"""
		takes input value x to return the value of f(x)
		"""
		return self.a*x**2+self.b*x+self.c


	def table(self,L,R,n):
		"""
		takes input left boundary, L, right boundary, R,
		and number of division, n to create a table with
		n divisions of x and the corresponding f(x) value
		"""
		x = np.linspace(L,R,n)
		tbl = np.zeros((n,2))
		for i in range(np.shape(x)[0]):
			tbl[i][0]= x[i] 
			tbl[i][1] = self.value(x[i])
		return tbl

	def roots(self):
		"""
		calculates the roots dependent on a, b and c
		"""
		r1 = (-self.b+sqrt(self.b**2.0-4*self.a*self.c))/(2*self.a)	
		r2 = (-self.b-sqrt(self.b**2.0-4*self.a*self.c))/(2*self.a)
		return r1,r2

def demonstration(a,b,c,x,L,R,n):
	"""
	demonstration of the output from the class Quadratic
	"""

	q = Quadratic(a,b,c)
	print 'value: \n',q.value(x)
	print 'table: \n',q.table(L,R,n)
	print 'roots: \n',q.roots()

from Quadratic import Quadratic,demonstration
print demonstration(1,2,3,0.5,0,4,2)

"""
python Quadratic.py
value: 
4.25
table: 
[[  0.   3.]
 [  4.  27.]]
roots: 
((-1+1.4142135623730951j), (-1-1.4142135623730951j))
None
value: 
4.25
table: 
[[  0.   3.]
 [  4.  27.]]
roots: 
((-1+1.4142135623730951j), (-1-1.4142135623730951j))
None
"""


