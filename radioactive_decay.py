#radioactive_decau.pu
import numpy as np

class Decau:
	def __init__(self,a):
		self.a = a

	def __call__(self,u):
		return -self.a*u

	def RK4(self, t0, tn, u0, n):
		t = np.zeros(n+1)
		u = np.zeros(n+1)
		u[0]=u0
		t[0]=t0
		dt = float(tn-t0)/n

		for k in range(n):
			t[k+1] = t[k]+dt
			K1 = dt*(self.__call__(u[k]))
			K2 = dt*(self.__call__(u[k]+0.5*K1))
			K3 = dt*(self.__call__(u[k]+0.5*K2))
			K4 = dt*(self.__call__(u[k]+K3))
			u[k+1] = u[k]+(1./6)*(K1+2*K2+2*K3+K4)
		return u,t


a = np.log(2)/5600
dec = Decau(a)

tn = 20000
t0=0
dt = 500
n = tn/dt
u0 = 1
# au = lambda u,t:  -a*u
u,t = dec.RK4(t0, tn, u0, n)
u_exact_final = np.exp(-a*tn)
print '%16s %16s' %('Computed value', 'Exact value')
print '%16.10s %16.10s' %(u[-1],u_exact_final)

