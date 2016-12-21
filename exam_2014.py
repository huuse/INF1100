#exam_2014.py

"""
1)
a) 2

b)
  3.00	2.90	4.80
  4.00	3.20 	-8.50
  5.00	4.30	4.50

c)24
"""
# def myfunc(a,b):
# 	s=0
# 	for k in a:
# 		s+= a[k]*b**k
# 	return s
# print myfunc({1:-1,3:1},3)
"""
d) {1:2,2:2,3:1}

e)True
"""

# # a = -2.3
# # print 'a=%.2f' %a
# a = {1:-1,3:1}
# b= {1:3,2:2}

# c = a.copy()
# print c
# for k in b:
# 	print k
# c[1]+=b[1]
# c[2]=b[2]
# print c
# # for k in b:
# # 	print k

# # 	if k in a:
# # 		print 'ok'
# # 		print k in a
# # 	else:
# # 		print 'not ok'


"""
2)

"""

# import numpy as np
# def ex2(t):
# 	if t<5:
# 		return 0
# 	else:
# 		return 0.4

# def test_ex2():
# 	tol = 1e-15
# 	t1 = 2
# 	t2 = 7
# 	expected1 = 0
# 	expected2 = 0.4
# 	computed1 = ex2(t1)
# 	computed2 = ex2(t2)
# 	success = abs(expected1-computed1)<tol \
# 	and abs(expected2-computed2)<tol
# 	msg = 'something is wrong'
# 	assert success, msg
# test_ex2()

"""
3)
a) 	1 0
	2 0
	3 0

b)
# """
# N=3
# from numpy import zeros
# y = zeros(N+1, int)
# # y[0] = 1
# for i in range(1, N+1):
# 	y[i] = i*y[i-1]
# 	print i,y[i]

"""
c)
"""
# def ex2c(n):
# 	N = n-1
# 	from numpy import zeros
# 	y = zeros(N+1, int)
# 	y[0] = 1
# 	for i in range(1, N+1):
# 		y[i] = i*y[i-1]
# 	return y

# print ex2c(14)
from numpy import zeros
def factorial(N):
	y = zeros(N+1,int)
	y[0] = 1
	for i in range(1,N+1):
		y[i] = i*y[i-1]
	return y
y_14=factorial(14)[-1]
print y_14

"""
d)
"""
# def test_ex2c():
# 	import numpy as np
# 	n = 5
# 	expected = np.asarray([1,1,2,6,24])
# 	computed = np.asarray(ex2c(n))
# 	success = np.all(expected == computed)
# 	msg = 'something is wrong'
# 	assert success, msg
# test_ex2c()


"""
4)
a)
"""
# def polyeval(x,p):
# 	s = 0
# 	for i in p:
# 		s += p[i]*x**i 
# 	return s
# print polyeval(2, {1:-1, 3:1})

"""
b)
"""
# def polyadd(p,q):
# 	r = q.copy()
# 	for i in p:
# 		if i in q:
# 			r[i] += p[i]
# 		else:
# 			r[i] = p[i]
# 	return r

# print polyadd({1:-1, 3:1},{1:3, 2:2})

"""
5
"""

# class Poly:
# 	def __init__(self,p):
# 		self.coeff = p

# 	def __call__(self, x):

# 		return self.polyeval(x, self.coeff)

# 	def __add__(self,other):
# 		result_dict = self.polyadd(self.coeff, other.coeff)
# 		return Poly(result_dict)

# 	def polyeval(self,x,p):
# 		p = self.coeff
# 		s = 0
# 		for i in p:
# 			s += p[i]*x**i 
# 		return s	
# 	def polyadd(self,p,q):
# 		r = q.copy()
# 		for i in p:
# 			if i in q:
# 				r[i] += p[i]
# 			else:
# 				r[i] = p[i]
# 		return r


# p1 = Poly({1:-1,3:1})
# print p1(3)
# p2 = Poly({1:3, 2:2})
# p3 = p1+p2
# print p3.coeff


"""
6)
"""

# class Poly:
# 	def __init__(self,p):
# 		self.coeff = p

# 	def __call__(self, x):

# 		return self.polyeval(x, self.coeff)

# 	def __add__(self,other):
# 		result_dict = self.polyadd(self.coeff, other.coeff)
# 		return Poly(result_dict)

# 	def polyeval(self,x,p):
# 		s = 0
# 		for i in p:
# 			s += p[i]*x**i 
# 		return s

# 	def polyadd(self,p,q):
# 		r = q.copy()
# 		for i in p:
# 			if i in q:
# 				r[i] += p[i]
# 			else:
# 				r[i] = p[i]
# 		return r

# 	def diff(self):
# 		p = self.coeff
# 		if 0 in p:
# 			del p[0]
# 		for i in p:
# 			p[i-1] = p[i]*i
# 			del p[i]
# 		return Poly(p)


# p1 = Poly({1:-1,3:1})
# print p1(3)
# p2 = Poly({1:3, 2:2})
# p3 = p1+p2
# print p3.coeff

# p4 = p3.diff()
# print p4.__class__.__name__
# print p4.coeff


"""
7)
a)
"""


# from ODESolver import ODESolver
# class RK2(ODESolver):
# 	def advance(self):
# 		f, x, y, k  = self.f, self.t, self.u, self.k	
# 		dx = x[k+1]-x[k]
# 		k1 = dx*f(y[k],x[k])
# 		k2 = dx*f(y[k]+0.5*k1, x[k]+0.5*dx)
# 		return y[k] + k2

"""
b)
"""

# from ODESolver import ODESolver
# # from exam_2014 import RK2


# def test_RK2():
# 	arg = lambda y,x: 2+(y-(2*x+3))**2
# 	tol = 1e-14
# 	import numpy as np
# 	xlst = np.linspace(0,10,20)
# 	expected = []
# 	for i in xlst:
# 		expected.append(2*i+3)
# 	init = 3
# 	solver = RK2(arg)
# 	solver.set_initial_condition(expected[0])
# 	computed,xes = solver.solve(xlst)

# 	success = np.all(abs(np.asarray(computed) - \
# 		np.asarray(expected))<tol)
# 	msg = 'doesnt work'
# 	assert success, msg

# test_RK2()
	
"""
8
"""
# from ODESolver import ODESolver

# import numpy as np
# import matplotlib.pyplot as plt

# S0 	= 1000
# I0 	= 2
# b 	= lambda t: 0.001
# q 	= 1/7.0
# d 	= 1/100.0
# T 	= 10



# # def p(t):
# # 	K = 5
# # 	if t<K:
# # 		return 0
# # 	else:
# # 		return 0.4
# p = lambda t: 0 if t<K else 0.4
# K=5


# def flu(S0, I0, b, q, d, p, T):
# 	def f(u,t):
# 		S,I,R,V = u
# 		return [-b(t)*S*I-p(t)*S+d*R,\
# 		b(t)*S*I-q*I, q*I-d*R, p(t)*S]
	
# 	t = np.linspace(0, T, 5*T+1)
# 	init = [S0, I0, 0, 0]

# 	solver = RK2(f)
# 	solver.set_initial_condition(init)
# 	y,t = solver.solve(t)
# 	S = y[:,0]
# 	I = y[:,1]
# 	R = y[:,2]
# 	V = y[:,3]
# 	return S,I,R,V,t


# S,I,R,V,t = flu(S0, I0, b, q, d, p, T)

# plt.plot(t,S,t,I,t,R,t,V)
# plt.legend(['S(t)','I(t)','R(t)','V(t)'])
# plt.show()

"""
9
"""

# def dump(filename, t, S, I, R, V):
# 	import numpy as np
# 	outfile = open(filename, 'w')
# 	outfile.write('%10.4s %10.4s %10.4s %10.4s %10.4s \n' \
# 		%('t   ','S   ','I   ','R   ','V   '))
# 	for i in range(len(t)):
# 		outfile.write('%10.4f %10.4f %10.4f %10.4f %10.4f \n'\
# 		 %(t[i],S[i],I[i],R[i],V[i]))
# 	outfile.close()

# dump('dumptest.txt',t,S,I,R,V)

# def dump(filename, t, S, I, R, V):
# 	import numpy as np
# 	outfile = open(filename, 'w')
# 	outfile.write('%10.4s %10.4s %10.4s %10.4s %10.4s \n' \
# 		%('t   ','S   ','I   ','R   ','V   '))
# 	for t_, S_, I_, R_, V_ in zip(t,S,I,R,V):
# 		outfile.write('%10.4f %10.4f %10.4f %10.4f %10.4f \n'\
# 		 %(t_,S_,I_,R_,V_))
# 	outfile.close()

# dump('dumptest.txt',t,S,I,R,V)

