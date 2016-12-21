#yx_ODE_FE_vs_RK4.py
import numpy as np

def RK4(f, x0, xn, y0, n):
	x = np.zeros(n+1)
	y = np.zeros(n+1)
	y[0]=y0
	x[0]=x0
	dx = float(xn-x0)/n

	for k in range(n):
		x[k+1] = x[k]+dx
		K1 = dx*f(y[k],x[k])
		K2 = dx*f(y[k]+0.5*K1,x[k]+0.5*dx)
		K3 = dx*f(y[k]+0.5*K2, x[k]+0.5*dx)
		K4 = dx*f(y[k]+K3, x[k]+dx)
		y[k+1] = y[k]+(1./6)*(K1+2*K2+2*K3+K4)
	return y,x

def ForwardEuler(f, x0, xn, y0, n):
	x = np.zeros(n+1)
	y = np.zeros(n+1)
	y[0]=y0
	x[0]=x0
	dx = float(xn-x0)/n
	print dx
	for k in range(n):
		x[k+1] = x[k]+dx
		y[k+1] = y[k]+dx*f(y[k],x[k])
	return y,x

f= lambda y,x: 1/(2*(y-1))
e = 0.001
y0 = 1 + np.sqrt(e)
x0 = 0
xn = 4
n = 4*2*2*2*2*2*2*2*2

yrk4,xrk4 = RK4(f, x0, xn, y0, n)
yfe,xfe = ForwardEuler(f, x0, xn, y0, n)


y_ex = lambda x: 1+np.sqrt(x+e)
y_lst_correct = [y_ex(xrk4[i]) for i in range(len(xrk4))]

import matplotlib.pyplot as plt
plt.plot(xrk4,yrk4,xfe,yfe,xrk4,y_lst_correct)
plt.legend(['rungekutta4', 'ForwardEuler', 'correct'])
plt.show()
