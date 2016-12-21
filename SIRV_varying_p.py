#SIRV_varying_p.py


#SIRV.py

#SIR_class.py
import numpy as np
import ODESolver
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


class ProblemSIR:
	def __init__(self, nu, beta, S0, I0, R0, V0, T, p):
		"""
		nu, beta: parameters in the ODE system
		S0, I0, R0: initial values
		T: simulation for t in [0,T]
		"""
		self.S0 = S0
		self.I0 = I0
		self.R0 = R0
		self.V0 = V0
		self.T = T
		if isinstance(nu, (float,int)): # number?
			self.nu = lambda t: nu
			# wrap as function
		elif callable(nu):
			self.nu = nu

		if isinstance(beta, (float,int)): # number?
			self.beta = lambda t: beta
			# wrap as function
		elif callable(beta):
			self.beta = beta
		if isinstance(p, (float,int)): # number?
			self.p = lambda t: p
			# wrap as function
		elif callable(p):
			self.p = p
			# store the other parameters
	def __call__(self, u, t):
		"""Right-hand side function of the ODE system."""
		S, I, R, V = u
		return [-self.beta(t)*S*I-self.p(t)*S,
		# S equation
		self.beta(t)*S*I-self.nu(t)*I,
		# I equation
		self.nu(t)*I,
		# R equation
		self.p(t)*S]
		# V equation



class SolverSIR:
	def __init__(self, problem, dt):
		self.problem, self.dt = problem, dt
	def solve(self, method=ODESolver.RungeKutta4):
		self.solver = method(self.problem)
		ic = [self.problem.S0, self.problem.I0, self.problem.R0, self.problem.V0]
		self.solver.set_initial_condition(ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0, self.problem.T, n+1)
		u, self.t = self.solver.solve(t)
		self.S, self.I, self.R, self.V= u[:,0], u[:,1], u[:,2], u[:,3]
	def plot(self):
		import matplotlib.pyplot as plt
		plt.plot(self.t,self.S,self.t,self.I,self.t,self.R,self.t,self.V)
		plt.legend(['S','I','R','V'],loc = 'best')
		plt.xlabel('time (days)')
		plt.ylabel('population')
		plt.show()





def p(t):

	if 6<= t <= 15:
		return 0.1
	else:
		return 0



# Example:
problem = ProblemSIR(nu=0.1, beta=0.0005,S0=1500, I0=1, R0=0, V0=0, T=60, p=p)
solver = SolverSIR(problem,dt)
solver.solve()
solver.plot()

"""
Kommentar: ser paa plot at max infected er på ca 440 naa 
,mot max infected er paa ca 50 individer 
hvis vaksinen blir brukt fra dag 1. 
Dette viser hvor viktig det er aa starte vaksineprogram
saa fort som mulig.
"""

