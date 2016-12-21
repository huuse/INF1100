#SIR.py

import numpy as np
from ODESolver import *
import matplotlib.pyplot as plt

S0 = 1500
I0 = 1
R0 = 0
v = 0.1
dt = 0.5
t0 = 0
tt = 60
nots = (tt-t0)/dt
t_lst = np.linspace(0, 600, nots+1)



U0 = [S0,I0,R0]

def f(u,t):
	v = 0.1
	S,I,R = u
	beta = 0.0005   # beta = 0.0001
	return [-beta*S*I, beta*S*I-v*I, v*I]



def terminate(u, t, step_no):
	tol = 1e-1
	S = u[step_no,0],u[step_no,1],u[step_no,2]
	S0 = u[0,0]
	I0 = u[0,1]
	R0 = u[0,2]
	return abs(sum(u[step_no])-sum(u[0]))>tol


solver = RungeKutta4(f)
solver.set_initial_condition(U0)
u, t = solver.solve(t_lst,terminate)



def plotting(u,t):

	S = u[:,0]
	I = u[:,1]
	R = u[:,2]

	plt.plot(t,S,t,I,t,R)
	plt.legend(['S','I','R'],loc = 'best')
	plt.xlabel('time (days)')
	plt.ylabel('population')
	plt.show()




plotting(u,t)


"""
Kommentar: Beta er smitteraten. 
ser paa plot at en hoeyere beta foerer til raskere spredning av sykdommen.
Ser man paa et lengere tidsforloep med beta = 0.0001 kan man se 
at ikke alle rekker aa bli smittet foer sykdommen har forsvunnet.
"""
