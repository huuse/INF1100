#exam_2012.py

"""
1)
"""
# from math import sqrt, exp, pi
# m = 0
# def f(x):
# 	return 1./(sqrt(2*pi))*exp(-0.5*(x-m)**2)

# print f(0.5)


"""
2)
"""
# from math import sqrt, exp, pi
# class Gaussian:
# 	def __init__(self,m):
# 		self.m = m
# 	def __call__(self,x):
# 		m = self.m
# 		return 1./(sqrt(2*pi))*exp(-0.5*(x-m)**2)



# f = Gaussian(m=2)
# value = f(2.5)
# print value


"""
3)
"""

# from math import sqrt, exp, pi
# import sys
# import numpy as np
# def f(x):
# 	return (1./sqrt(2*pi))*exp(-0.5*(x-m)**2)

# if len(sys.argv)<3:
# 	print 'Usage: Gaussian.py m, x1, x2 ...'
# 	sys.exit(1)
# m = int(sys.argv[1])
# for x in sys.argv[2:]:
# 	x = float(x)
# 	print '%.3E' %(f(x))


# def f(x):
# 	print type(x)
# 	if len(x) >1:
# 		xlst = np.asarray(x)
# 	else:
# 		xlst = x[0]
# 	return 1./(sqrt(2*np.pi))*np.e**(-0.5*(xlst-m)**2)


"""
4)

a)
Newton

b)
1.0 0

c)
4 2 9

d)
3
[1,2,3,0,1,2]
ForwardEuler

e)
6
"""

"""
5)
in PowerFunction constructor
in composite_function
in __call__
in reduce, x: [0. 1. 4.]
1.0 0.0
2.0 1.0
3.0 2.0
"""

"""
6)
"""

# infile = open('ex6data.txt','r')
# x =[]
# y=[]
# for line in infile:
# 	word = line.split()
# 	x.append(float(word[0]))
# 	y.append(float(word[1]))
# infile.close()
# import matplotlib.pyplot as plt

# plt.plot(x,y,color='r')
# plt.show()

"""
7)
"""
# import numpy as np
# infile = open('ex6data.txt','r')
# x =[]
# y=[]
# xu = []
# u = []
# for line in infile:
# 	word = line.split()
# 	x.append(float(word[0]))
# 	y.append(float(word[1]))
# 	if len(word)>2:
# 		xu.append(float(word[0]))
# 		u.append(float(word[2]))

# infile.close()
# import matplotlib.pyplot as plt
# plt.plot(x,y,'r',xu,u,'bo')
# plt.show()



"""
8)
"""
# import numpy as np
# x = np.array([-1.000000,-0.959184,-0.918367,-0.877551])
# y = np.array([-0.76E-2, -0.74E-2, -0.72E-2, -0.70E-2])
# uncertainty = np.array([0.1432, None, None, -0.9078])

# def dump_data(filename, x, y, uncertainty):
# 	outfile = open(filename,'w')
# 	size = len(uncertainty)
# 	for i in range(size):
# 		outfile.write('%14.6f %12.2E' %(float(x[i]),float(y[i])))
# 		if isinstance(uncertainty[i],float):
# 			outfile.write('%12.4f' %(float(uncertainty[i])))
# 		outfile.write('\n')
# 	outfile.close()	
# dump_data('ex8_out.txt',x,y,uncertainty)

"""
9)
"""
# from random import randint
# import numpy as np
# N = 10000
# flip = 20
# money = 0
# carlo = np.zeros((N,flip))
# for i in range(N):
# 	for j in range(flip):
# 		carlo[i][j] = randint(0,1)
# for case in carlo:
# 	if np.sum(case)>=15:
# 		money += 400

# 	else:
# 		money -= 10


"""
10)
"""
# from TimeIntegral import TimeIntegral
# from numpy import np
# import random

# class MonteCarlo(TimeIntegral):
# 	def initialize(self):
# 		T, n = self.T, self.n
# 		self.t. = np.random.uniform(0,T,n+1)
# 		w = T/float(n+1)
# 		self.w = np.zeros(len(self.t))+w
# def _test(constant=2.5):
# 	def G(t):
# 		return constant

# 	T = 10
# 	n = 4
# 	integrator = MonteCarlo(G, T, n)
# 	print integrator.compute(), 'exact:', T*constant
# _test()

















