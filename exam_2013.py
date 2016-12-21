#exam_2013.py

"""
1)
"""

# b = lambda t: 0.001 if t<6 else 0.002

# a = b(4)

"""
2)
0
3
dog
9
10
toof
"""
# import numpy as np
# a = np.linspace(8,10,3)
# print a
# b = a[1:-1]
# print b
# a[1] = 10
# print b
# print int(b[0])

"""
3)
 dog goes woof
 cat goes meow
 bird goes tweet
 and mouse goes squeak
 cow goes moo
 frog goes croak
 and the elephant goes toot
 duck says quack
 and fish goes blub
 and the seal goes ow ow ow

 Continue as you like: 
"""

"""
4)
OK!
"""

"""
5)
2.0
4.0
"""

# from math import exp
# print exp(2)

"""
6)
"""
# def poly_diff(d):
# 	r = {}
# 	for j in d:
# 		if j >=1:
# 			r[j-1] = j*d[j]
# 	return r
# print poly_diff({0:2,6:-5})


"""
7)
"""
# def sum_file(inputname, outputname):
# 	import numpy as np
# 	infile = open(inputname, 'r')
# 	outfile = open(outputname, 'w')
# 	for line in infile:
# 		word = line.split()
# 		summ = 0
# 		for i in word:
# 			outfile.write('%7.2f' %float(i))
# 			summ += float(i)
# 		outfile.write('%7.2f \n' % summ)
# 	infile.close()
# 	outfile.close()
# sum_file('ex7.txt','ex7_sum.txt')


"""
8)
"""

import sys
import numpy as np
from random import randint
try:

	n = int(sys.argv[1]) 
	m = int(sys.argv[2])
except IndexError:
	print 'n and m must be given as command-line arguments!'
	sys.exit(1)

except ValueError:
	print 'n and m must be integers' 
	sys.exit(1)
N = 1000
success = 0
for i in range(N):

	toss = []
	[toss.append(randint(0,1)) for i in range(n)]
	if np.sum(toss)>=m:
		success +=1

p = success/float(N)
print p


"""
9)
"""

# from ODESolver import ODESolver

# class Heun(ODESolver):
# 	def advance(self):
# 		u, f, k, t = self.u, self.f, self.k, self.t
# 		dt = t[k+1]-t[k]
# 		u_ = u[k] + dt*f(u[k],t[k])
# 		return u[k] + 0.5*dt*f(u[k],t[k])+0.5*dt*f(u_,t[k+1])

"""
10)
"""

# from ODESolver import ODESolver
# import numpy as np
# class IteratedMidpointMethod(ODESolver):

# 	def advance(self):
# 		u, t, f, k = self.u, self.t, self.f, self.k
# 		N = 100
# 		dt = t[k+1]-t[k]
# 		vold = u[k]
# 		for q in range(N):
# 			vnew = (u[k]+0.5*dt*(f(vold,t[k+1])+f(u[k],t[k])))
# 			vold = vnew
# 		return vnew





# solver = IteratedMidpointMethod(f = lambda y, x: 1.0/y)
# solver.set_initial_condition(U0=1)
# y,x = solver.solve(time_points=np.linspace(0,5,20))
# print y,x
# import matplotlib.pyplot as plt
# import matplotlib.style
# matplotlib.style.use('seaborn-darkgrid')

# plt.plot(x,y)
# plt.show()


"""
11)
"""
# from ODESolver import ODESolver
# from ODESolver import ForwardEuler
# import numpy as np

# def flu(S0, I0, b, q, T):
# 	def f(u,t):
# 		S,I,R = u
# 		return [-b(t)*S*I, b(t)*S*I-q*I, q*I]
	
# 	solver = ForwardEuler(f)
# 	init = [S0,I0,0]
# 	solver.set_initial_condition(init)
# 	ts = np.linspace(0,T,5*T+1)
# 	x,t = solver.solve(ts)
# 	S = x[:,0]
# 	I = x[:,1]
# 	R = x[:,2]
# 	return S,I,R,t
# S0=100
# I0=1
# q=1./7
# T=40
# b = lambda t: 0.01 if t<5 else 0.002
# S,I,R,t = flu(S0, I0, b, q, T)

# import matplotlib.pyplot as plt
# import matplotlib.style
# matplotlib.style.use('seaborn-darkgrid')
# plt.plot(t,S,t,I,t,R)
# plt.legend(['S','I','R'])
# plt.show()







