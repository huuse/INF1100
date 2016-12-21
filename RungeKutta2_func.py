#RungeKutta2_func.py
import numpy as np
import matplotlib.pyplot as plt




def mk_ForwardEuler(f, T, U0, n):
	t = np.zeros(n+1)
	u = np.zeros(n+1)
	u[0]=U0
	t[0]=0
	dt = float(T)/n

	for k in range(n):
		t[k+1] = t[k]+dt
		K1 = dt*f(u[k],t[k])
		K2 = dt*f(u[k]+0.5*K1,t[k]+0.5*dt)
		u[k+1] = u[k]+K2
	return u,t


def mk_f(u,t):
	return u

T=4
u,t = mk_ForwardEuler(mk_f, T, U0=1, n=25)
t_exact = np.linspace(0,T,400)
u_exact = np.exp(t_exact)
plt.plot(t_exact,u_exact, 'r-')
plt.plot(t,u, 'b-')
plt.legend(['exact solution','2nd-order Runge-Kutta solution'])
plt.show()


"""
python RungeKutta2_func.py
"""