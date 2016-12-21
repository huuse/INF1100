#general_2016.py

"""
1.4) length_conversion.py
"""
# inch = 2.54 #cm
# foot = 12 #inch
# yard = 3 #foot
# Bmile = 1760 #yard

# length = 640
# lenghtcm = float(640*100)
# ininch = lenghtcm/inch
# infoot = ininch/foot
# inyard = infoot/yard
# inBmile = inyard/Bmile
# print '%.2f meter = %.2f inch = %.2f foot = %.2f yard = %.4f British mile'\
# %(length,ininch,infoot,inyard,inBmile)

"""
1.11) kick.py
"""
# from math import pi
# g = 9.81 #m/s**2
# da = 1.2 #kg/m**3
# a = 0.11 #m
# m = 0.43 #kg
# A = pi*a**2 #m**2
# CD = 0.2 #
# V1 = 120 #km/h
# V2 = 10 #km/h
# ms = 1000.0/(60*60)
# V1ms = V1*ms
# V2ms = V2*ms
# Fd1 = 0.5*CD*da*A*V1ms**2
# Fd2 = 0.5*CD*da*A*V2ms**2
# Fg = m*g

# print 'Hard kick: Fg = %.1f N, Fd = %.1f N, ratio: %.1f. \n \
# Soft kick: Fg = %.1f N, Fd = %.1f N, ratio: %.5f' \
# %(Fg,Fd1,Fd1/Fg,Fg,Fd2,Fd2/Fg)


"""
E41) SIR.py
"""
from ODESolver2 import ODESolver
from ODESolver2 import RungeKutta4
import numpy as np
import matplotlib.pyplot as plt
# import matplotlib.style
# matplotlib.style.use('seaborn-darkgrid')

S0 = 1500
I0 = 1
R0 = 0
v = 0.1
dt = 0.5
tp = np.linspace(0,60,120)
b = 0.0005
#b = 0.0001

def SIR(S0,I0,R0,v,dt,tp,b):
	def f(u,t):
		S,I,R = u
		return [-b*S*I, b*S*I-v*I, v*I]

	def terminate(u,t,step_no):
		C = u[step_no,0]+ u[step_no,1]+ u[step_no,2]
		C0 = u[0,0]+ u[0,1]+ u[0,2]
		tol = 1e-12
		success = abs(C-C0)>tol
		if success:
			print 'stopped due to S+I+R !=0 (tol=%.3E' %tol
		return success
	solver = RungeKutta4(f)
	init = [S0,I0,R0]
	solver.set_initial_condition(init)
	u,t = solver.solve(tp,terminate)

	S,I,R = u[:,0],u[:,1],u[:,2]
	


	def vizual_SIR(S,I,R,t):
		plt.plot(t,S,t,I,t,R)
		plt.legend(['S','I','R'])
		plt.show()

	vizual_SIR(S,I,R,t)

# SIR(S0,I0,R0,v,dt,tp,b)



"""
E.42) SIR_class.py
"""
import ODESolver2
class ProblemSIR:
	def __init__(self,nu, beta, S0, I0, R0, T):

		if isinstance(nu, (float,int)):
			self.nu =lambda t: nu

		elif callable(nu):
			self.nu = nu

		if isinstance(beta, (float,int)):
			self.beta =lambda t: beta

		elif callable(beta):
			self.beta = beta

		self.S0 = S0
		self.I0 = I0
		self.R0 = R0
		self.T = T



	def __call__(self, u ,t):
		S,I,R = u
		return [-self.beta(t)*S*I, \
		self.beta(t)*S*I-self.nu(t)*I,\
		self.nu(t)*I]



class SolverSIR:
	def __init__(self, problem, dt):
		self.problem, self.dt = problem, dt
		self.ic = [self.problem.S0, self.problem.I0, \
		self.problem.R0]

	def solve(self, method=ODESolver2.RungeKutta4):
		self.solver = method(self.problem)

		self.solver.set_initial_condition(self.ic)
		n = int(round(self.problem.T/float(self.dt)))
		t = np.linspace(0, self.problem.T, n+1)
		self.u, self.t = self.solver.solve(t)

	def plot(self):
		self.S, self.I, self.R = self.u[:,0], self.u[:,1], self.u[:,2]
		plt.plot(self.t,self.S,self.t,self.I,self.t,self.R)
		plt.legend(['S','I','R'])
		plt.show()



# problem = ProblemSIR(beta=lambda t: 0.0005 if t<= 12 \
#  else 0.0001,\
# 	nu=0.1, S0=1500, I0=1, R0=0, T=60)
# solver = SolverSIR(problem,dt)
# solver.solve()
# solver.plot()


"""
E.43) SIRV.py
"""

class SIRV(ProblemSIR):
	def __init__(self,nu, beta, S0, I0, R0, T,p,V0):
		ProblemSIR.__init__(self,nu, beta, S0, I0, R0, T)
		self.p = p
		self.V0 = V0


	def __call__(self,u,t):
		S,I,R,V = u
		return [-self.beta(t)*S*I-self.p*S,\
		self.beta(t)*S*I-self.nu(t)*I, self.nu(t)*I,\
		self.p*S]

class SolverSIRV(SolverSIR):
	def __init__(self, problem, dt):
		SolverSIR.__init__(self, problem,dt)
		self.ic = [self.problem.S0, self.problem.I0, \
		self.problem.R0, self.problem.V0]	

	def plot(self):
		self.S, self.I, self.R, self.V = self.u[:,0], \
		self.u[:,1], self.u[:,2], self.u[:,3]
		plt.plot(self.t,self.S,self.t,self.I,\
			self.t,self.R,self.t,self.V)
		plt.legend(['S','I','R','V'])
		plt.show()









"""
E.44) SIRV_Varying_p.py
"""
class SIRV_varying_p(SIRV):
	def __call__(self,u,t):
		S,I,R,V = u
		return [-self.beta(t)*S*I-self.p(t)*S,\
		self.beta(t)*S*I-self.nu(t)*I, \
		self.nu(t)*I,self.p(t)*S]



# problem = SIRV_varying_p(beta=lambda t: 0.0005 if t<= 12 \
# else 0.0001,\
# nu=0.1, S0=1500, I0=1, R0=0, T=60, p= lambda t: \
# 0.1 if 6<=t<=15 else 0, V0=0)
# solver = SolverSIRV(problem,dt)
# solver.solve()
# solver.plot()



"""
E.45) SIRV_optimal_duration.py
"""
class SIRV_optimal_duration(SIRV_varying_p):
	def __init__(self,nu, beta, S0, I0, R0, T,p,V0,Vt):
		SIRV_varying_p.__init__(self,nu, beta, S0, I0, R0, T,p,V0)
		self.Vt = Vt

class SolverSIRV_optimal_duration(SolverSIRV):
		

	def plot(self):
		self.S, self.I, self.R, self.V = self.u[:,0], \
		self.u[:,1], self.u[:,2], self.u[:,3]
		# plt.title('testestset')
		plt.plot(self.t,self.S,self.t,self.I,\
			self.t,self.R,self.t,self.V,hold=True)
		plt.legend(['S','I','R','V'])
		
		plt.show()

# Imax = []
# for Vt in range(0,31):

# 	def p(t):
# 		if 6<=t<=15+Vt:
# 			return 0.1
# 		else:
# 			return 0
# 	problem = SIRV_optimal_duration(beta=lambda t: 0.0005 if t<= 12 \
# 	else 0.0001,\
# 	nu=0.1, S0=1500, I0=1, R0=0, T=60, p=p, V0=0, Vt=Vt)
# 	solver = SolverSIRV_optimal_duration(problem,dt)
# 	solver.solve()
# 	Imax.append(max(solver.u[:,1]))
# 	print max(solver.u[:,1])
# 	solver.plot()
# print max(Imax)
# print len(Imax)
# Vtlst= np.linspace(0,Vt+1,Vt+1)
# print len(Vtlst)
# plt.plot(Vtlst,Imax)
# plt.show()


























