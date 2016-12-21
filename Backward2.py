#Backward2.py

import numpy as np


class Diff:
	def __init__(self, f, h=1e-5):
		self.f = f
		self.h = h

class bw1(Diff):
	def __call__(self, x):
		f = self.f
		h = self.h
		return (f(x)-f(x-h))/float(h)


class bw2(Diff):
	def __call__(self, x):
		f = self.f
		h = self.h
		return (f(x-2*h)-4*f(x-h)+3*f(x))/float(h)





def gt(t):
	return np.exp(-t)



k = 1+14
h = np.zeros(k)
gd1 = np.zeros(k)
gd2 = np.zeros(k)

for i in range(k):
	h[i] = 2**(-k)

	bw11 = bw1(gt, h[i])
	gd1[i] = bw11(x=2)
	bw22 = bw1(gt, h[i])
	gd2[i] = bw22(x=2)



# print gd1
# print gd2
error = np.abs(gd1-gd2)
print error


"""
python Backward2.py
[ 0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.  0.]
"""
