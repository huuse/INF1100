#kjernliekunta4.py

# from math import sqrt
# import matplotlib.pyplot as plt

# # f: function to solve du/dt=f(u,t)
# # t0: initial value of t
# # tN: final value of t
# # u0: initial value of u
# # N: number of steps
# def RungaKutta4(f, x0, xN, y0, N):
#         delta_x = (xN-x0) / float(N)
#         y = y0
#         x = x0
#         y_list = []
#         x_list = []
#         y_list.append(y)
#         x_list.append(x)
#         for i in range(N):
#                 K1 = delta_x*f(y)
#                 K2 = delta_x*f(y+0.5*K1)
#                 K3 = delta_x*f(y+0.5*K2)
# 		K4 = delta_x*f(y+K3)
# 		y += 1./6*(K1+K2+K3+K4)
#                 x += delta_x
#                 y_list.append(y)
#                 x_list.append(x)
#         return y_list, x_list


# def ForwardEuler(f, x0, xN, y0, N):
# 	delta_x = (xN-x0) / float(N)
# 	y = y0
# 	x = x0
# 	y_list = []
# 	x_list = []
# 	y_list.append(y)
# 	x_list.append(x)
# 	for i in range(N):
# 		y += delta_x*f(y)
# 		x += delta_x
# 		y_list.append(y)
# 		x_list.append(x)
# 	return y_list, x_list

# f = lambda y: 1/(2*(y-1))
# e = 0.001
# y0 = 1 + sqrt(e)
# x0 = 0
# xN = 4
# N = 2*2*2*2*2*2*4

# y_rk, x_rk = RungaKutta4(f,x0,xN,y0,N)
# y_fe, x_fe = ForwardEuler(f,x0,xN,y0,N)

# y_exact = lambda x: 1+sqrt(x+e)
# y_exact_lst = []
# for i in range(len(x_rk)):
# 	y_exact_lst.append(y_exact(x_rk[i]))

# plt.plot(x_rk,y_rk,x_rk,y_fe,x_rk,y_exact_lst)
# plt.legend(['RK4','Forward Euler','Exact'],loc='best')
# plt.show()





from math import log, exp
class Decay:
	def __init__(self,a):
		self.a = a

	def __call__(self,u):
		return -self.a*u

	# Use rk4 to solve the ode
	def RungaKutta4(self,t0, tN, u0, N):
	        delta_t = (tN-t0) / float(N)
		u = u0
		t = t0
		u_list = []
		t_list = []
		u_list.append(u)
		t_list.append(t)
		for i in range(N):
			K1 = delta_t*self.__call__(u)
			K2 = delta_t*self.__call__(u+0.5*K1)
			K3 = delta_t*self.__call__(u+0.5*K2)
			K4 = delta_t*self.__call__(u+K3)
			u += 1./6*(K1+2*K2+2*K3+K4)
			t += delta_t
			u_list.append(u)
			t_list.append(t)
		return u_list, t_list



a = log(2)/5600
dec = Decay(a) 

t_final = 20000
t_start = 0  # adding zero afterwards
delta_t = 500
N = t_final/delta_t
u0 = 1

u, t = dec.RungaKutta4(t_start,t_final, u0, N)
u_exact_final = exp(-a*t_final)

print '%16s %16s' %('Computed value','Exact value')
print '%16.10f %16.10f' %(u[-1], u_exact_final)



