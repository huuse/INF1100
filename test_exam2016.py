#test_exam2016.py

# print '4' in '37.5 degrees'

# for k in range(2,5,2):
# 	print k


# q = [['a','b','c'], ['d', 'e', 'f'], ['g', 'h']]
# print q[1]
# print q[-1][-1]


# import sys
 

# C = '20.0 degrees'
 
 

# try:
 

# 	C = float(C)
 

# except ValueError:
 

# 	print 'Cannot convert %s to float' %type(C)
 

# 	sys.exit(1)
 

# F = 9.0*C/5 + 32
 

# print '%gC is %.1fF' % (C, F)
 


# def test_sum():
 
# 	expected = 1+2+3+4+5
 
# 	computed = sum(range(6))
 

# 	asset expected == computed
 

# test_sum()
#  


# def funct(x):
#     if x<=0:
#         return -x
#     else:
#         return x

# def test_funct():
#     tol = 1e-29
#     x = 1
#     expected = 1
    
#     computed = funct(x)
#     assert abs(expected-computed)< tol

# test_funct()

# def funct(x):
#     if x<=0:
#         return -x
#     else:
#         return x

# def test_funct():
#     tol = 1e-12
#     x1 = -1
#     expected1 = 13
#     computed1 = funct(x1)
    
#     x2 = 2
#     expected2 = 2
#     computed2 = funct(x2)
    
#     assert abs(expected1-computed1)< tol
#     assert abs(expected2-computed2)< tol
# test_funct()

# infile = open('summer.txt', 'r')
# print type(infile)
# infile.readline()
# for line in infile:
# 	month, rain = line.split()
# 	rain = float(rain)
# 	print 'In %s, total rainfall was %.2f' %(month,rain)

# def add(a,b):
# 	return a + b

# print add(1,2)
# print add([1,2,3],[0,1,2])


# class Y:
# 	def __init__(self, v0):
# 		self.v0 = v0

# 	def __str__(self):
# 		return 'v0*t - 0.5*g*t**2; v0=%g' % self.v0
# y = Y(5)
# print y

# from random import randint

# N = 1000
# heads = 0
# for i in range(N):
# 	result = randint(4,6)
# 	if result ==5:
# 		heads +=1
# p = heads/N
# print heads

# def mtcarlos(n):
#     import numpy as np
#     from random import randint
#     N = 1000
#     throws = np.random.random_integers(1,6, size=(N,n))
#     success = np.sum(np.sum(throws ==6,axis=1)>=1)
#     return float(success)/N

# print mtcarlos(1)

# class Polynomial:
# 	def __init__(self, coefficients):
# 		self.coeff = coefficients
# 	def __call__(self, x):
# 		s=0
# 		for i in range(len(self.coeff)):
# 			s +=self.coeff[i]*x**i
# 		return s
# 	def __add__(self, other):
# 		# Start with the longest list and add in the other
# 		if len(self.coeff) >len(other.coeff):
# 			result_coeff =self.coeff[:]  # copy!
# 			for i in range(len(other.coeff)):
# 				result_coeff[i] += other.coeff[i]
# 		else:
# 			result_coeff = other.coeff[:] # copy!
# 			for i in range(len(self.coeff)):
# 				result_coeff[i] +=self.coeff[i]
# 		return Polynomial(result_coeff)

# from Polynomial import Polynomial
# p1 = Polynomial([1,1,1])
# p2 = Polynomial([0,0,0,5])
# p3 = p1+p2
# p3(1.0)
# print p3.__class__
# p4 = p3.diff()
# print p4(1)
# print p4.__class__.__name__
# print p4.coeff


# print taylor_exp(3)

# def test_taylor_exp():
# 	from Polynomial import Polynomial
# 	from taylor_exp import taylor_exp
# 	tol = 1e-12
# 	N=3
# 	expected = 2.52
# 	computed_temp = taylor_exp(N)
# 	computed = computed_temp(1)

# 	success = abs(expected-computed)<tol
# 	msg = 'something is wrong'
# 	assert success, msg
	

# test_taylor_exp()


# from ODESolver import ODESolver
# print 'her'
# # class Kutta3(ODESolver):
# # 	print 'her'
# # 	def advance(self):
# # 		y, f, k, t = self.u, self.f, self.k, self.t
# # 		dt = t[k+1]-t[k]
# # 		dt2 = dt/2.0
# # 		k1 = dt*f(y[k], t[k])
# # 		k2 = dt*f(y[k]+0.5*k1, t[k]+ dt2)
# # 		k3 = dt*f(y[k]-k1+2*k2, t[k] + dt)
# # 		ynew = yk +(1/6.0)*(k1+4*k2+k3)
# # 		return ynew
# print 'her'
from ODESolver import ODESolver
class Kutta3(ODESolver):
    def advance(self):
        u,f,k,t = self.u, self.f, self.k, self.t
        dt = t[k+1] - t[k]
        K1 = dt*f(u[k], t[k])
        K2 = dt*f(u[k]+0.5*K1, t[k] + 0.5*dt)
        K3 = dt*f(u[k] - K1 + 2*K2, t[k] + dt)
        unew = u[k] + (1/6.0)*(K1+4*K2+K3)
        return unew

def test_Kutta3():
	tol=1e-12
	import numpy as np
	f = lambda y, t: 2

	solver = Kutta3(f)
	solver.set_initial_condition(1)
	t = np.linspace(0,20,40)
	computed,t = solver.solve(t)
	expected = np.asarray([2*i+1 for i in t])

	success = np.all(computed==expected)
	msg = 'didnt work'
	assert success, msg


test_Kutta3()


#777777777777777777777777777777777777777777777777777777777777

# import numpy as np
# def arg(u,t):
# 	S,I,R = u
# 	global d
# 	global mu
# 	global q
# 	return [sigma(t)-b(t)*S*I+d*R-mu*S, b(t)*S*I-q*I-mu*I, q*I-d*R-mu*R]

# def SIR(S0, I0,sigma,mu,b,q,d, T):
# 	from ODESolver import ODESolver
# 	from ODESolver import RungeKutta4
# 	import numpy as np
# 	t = np.linspace(0, T, T*10)
# 	init = [S0, I0, 0]
	

# 	solver = RungeKutta4(arg)
# 	solver.set_initial_condition(init)
# 	y,t = solver.solve(t)
# 	S =y[:,0]
# 	I =y[:,1]
# 	R =y[:,2]

# 	return t,S,I,R

# S0=1000
# I0=2
# sigma= lambda t :10
# mu = 1/100.0
# b = lambda t :1/1000.0
# q = 1/7.
# d = 1/100.0
# T=40
# t,S,I,R = SIR(S0,I0,sigma,mu,b,q,d,T)
# from matplotlib.pyplot import *
# plot(t,S,t,I,t,R)
# show()

# u = [1,2,3,4,5,6]
# print u[2:4]






