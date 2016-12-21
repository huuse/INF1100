#exam_2015_again.py

"""
1.1)
False
"""

"""
1.2)
0
"""

"""
1.3)
['d','e','f']
h
"""
# q = [['a','b','c'],['d','e','f',],['g','h']]
# print q[1]
# print q[-1][-1]

"""
1.4)
Cannot convert <tye 'str'> to float
"""
# import sys
# C = '20.0 degrees'

# try:
# 	C = float(C)
# except ValueError:
# 	print 'cannot convert %s to float'%type(C)
# 	sys.exit(1)
# F = 9.0*C/5 +32
# print '%gC is %.1fF' % (C, F)
"""
1.5)
asset expected == computed
		
SyntaxError: Invalid syntax
"""
# def test_sum():
# 	expected = 1+2+3+4+5
# 	computed = sum(range(6))
# 	assert expected == computed
# test_sum()

"""
2)
"""
# y = lambda x: -x if x<=0 else x

# def ex2(x):
# 	if x<=0:
# 		return -x
# 	else:
# 		return x

# def test_ex2():
# 	x1=0
# 	x2=1
# 	expected1 = -x1
# 	expected2 = x2
# 	computed1 = y(x1)
# 	computed2 = y(x2)
# 	tol = 1e-14
# 	success = abs(expected1-computed1)<tol \
# and abs(expected2-computed2)<tol
# 	assert success

# test_ex2()

"""
3.1)
SyntaxError: invalid syntax
"""
# infile = open('summer.txt')
# infile.readline
# for line in infile:
# 	month, rain = line.split()
# 	rain = float(rain
# 	print 'In %s, total rainfall was %.2f' %(month,rain)


"""
3.2)
3
[1, 2, 3, 0, 1, 2]
"""
# def add(a, b):
# 	return a + b

# print add(1,2)
# print add([1,2,3],[0,1,2])

"""
3.3)
SyntaxError: invalid syntax
"""
# method1 = 'ForwardEuler'
# method2 = method1
# method1 = 'RK2'
# print method 2

"""
3.4)
v0*t - 0.5*g*t**2; v0=5
"""
# class Y:
# 	def __init__(self, v0):
# 		self.v0 = v0

# 	def __str__(self):
# 		return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0
# y = Y(5)
# print y

"""
3.5)
0
"""
# from random import randint
# N = 1000
# heads = 0
# for i in range(N):
# 	result = randint(0,1)
# 	if result == 0:
# 		heads += 1

# p = heads/N
# print p

"""
4.1)
"""
# from random import randint
# def carlo(n):
# 	N=1000
# 	six = 0
# 	for i in range(N):
# 		test = []
# 		for i in range(n):
# 			test.append(randint(1,6))
# 		if 6 in test:
# 			six += 1
# 	return six/float(N)
# print carlo(10)


"""
4.2)
"""
# import numpy as np
# def carlo(n):
# 	N = 1000
# 	test = np.random.random_integers(1,6,(N,n))
# 	success = np.sum(np.sum(test ==6,axis=1)>=1)
# 	return success/float(N)
# print carlo(10)


"""
5.1)a
8.0
"""
# from Polynomial import Polynomial
# p1 = Polynomial([1,1,1])
# p2 = Polynomial([0,0,0,5])
# p3 = p1 + p2
# print p3(1.0)
"""
5.2)b
"""
# from math import factorial

# def taylor_exp(N):
# 	from Polynomial import Polynomial
# 	poly = []
# 	for i in range(N):
# 		poly.append(1./factorial(i))
# 	return Polynomial(poly)

# case = taylor_exp(4)
# print case.__class__.__name__
# print case.coeff
"""
5.3)c
"""

# from Polynomial import Polynomial

# def test_taylor_exp():
# 	N = 3
# 	x = 2.0
# 	tol = 1e-14
# 	# expected = 5.0
# 	def expected3(x):
# 			return 	x**0/factorial(0)+ x**1/factorial(1)+ \
# 	x**2/factorial(2)
# 	instance = taylor_exp(N)
# 	computed = instance(x)
# 	success =  abs(expected3(x)-computed)<tol
# 	assert success
# test_taylor_exp()

"""
5.4)d
"""

# def diff(self):

# 	# poly = self.coeff.copy()
# 	# for i in range(1,poly):
# 	# 	poly[i-1] = poly[i]*i
# 	# del poly[-1]
# 	l = []
# 	print self.coeff
# 	for i in range(len(self.coeff)-1):
# 		l.append(self.coeff[i+1]*(i+1))
# 	print l
# 	return Polynomial(l) 

# p4 = p3.diff()
# print p4.__class__.__name__
# print p4.coeff


"""
5.5)e
"""

# def test_diff():
# 	x = 2
# 	p = Polynomial([1,1,1,5])
# 	tol = 1e-14
# 	expected = 1+2*2**1+15*2**2
# 	pd = p.diff()
# 	computed = pd(x)
# 	success = abs(expected-computed)<tol
# 	assert success
# test_diff()

"""
6.1)
"""
# from ODESolver import ODESolver
# import numpy as np
# class Kutta3(ODESolver):
# 	def advance(self):
# 		y, f, k, t = self.u, self.f, self.k, self.t
# 		dt = t[k+1] - t[k]
# 		K1 = dt*f(y[k], t[k])
# 		K2 = dt*f(y[k]+0.5*K1, t[k] +0.5*dt)
# 		K3 = dt*f(y[k]-K1 + 2*K2, t[k] + dt)
# 		return y[k]+(1/6.0)*(K1 + 4*K2 + K3)

"""
6.2)
"""	
# def test_Kutta3():
# 	f = lambda y, t : 2.0
# 	Y0 = 1.0
# 	tp = np.linspace(0,10,20)
# 	solver = Kutta3(f)
# 	solver.set_initial_condition(Y0)
# 	y,t = solver.solve(tp)
# 	computed = np.asarray(y)
# 	calc = []
# 	for t in tp:
# 		calc.append(2.0*t+1)
# 	calculated = np.asarray(calc)
# 	tol = 1e-14
# 	success = all(abs(calculated-computed)<tol)
# 	assert success

# test_Kutta3()


"""
7)
"""

# from ODESolver import ODESolver
# from ODESolver import RungeKutta4
# import numpy as np
# S0 = 1000
# I0 = 2
# simga = lambda t: 10.0
# mu = 1.0/100
# b = lambda t: 1.0/1000
# q = 1.0/7
# d = 1.0/100
# T = 40

# def SIR(S0, I0, simga, mu, b, q, d, T):
# 	def f(u,t):
# 		S,I,R = u
# 		return [simga(t)-b(t)*S*I+d*R-mu*S,\
# 		b(t)*S*I-q*I-mu*I, q*I-d*R-mu*R]
# 	solver = RungeKutta4(f)
# 	init = [S0,I0,0]
# 	solver.set_initial_condition(init)
# 	tp = np.linspace(0,T,10*T+1)
# 	y,t = solver.solve(tp)
# 	S,I,R = y[:,0],y[:,1],y[:,2]
# 	return S,I,R,t

# import matplotlib.pyplot as plt
# import matplotlib.style
# matplotlib.style.use('seaborn-darkgrid')
# S,I,R,t = SIR(S0, I0, simga, mu, b, q, d, T)
# plt.plot(t,S,t,I,t,R)
# plt.legend(['S','I','R'])
# plt.show()















