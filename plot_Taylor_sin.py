#plot_Taylor_sin.py

from math import factorial, pi, sin
from matplotlib.pyplot import *
import numpy as np




def S(x,n):
	S = [(-1)**(j)*x**(2.*j+1)/(factorial(2*j+1)) for j in range(n+1)]
	return np.sum(S, axis=0)


x = np.linspace(0,4*pi,100)
n = np.array((1,2,3,6,12))



Slst = [S(x,ni) for ni in n]



figure('plot_Taylor_sin')
for i in range(n.shape[0]):
	plot(x, Slst[i])
	hold('on')
plot(x,np.sin(x))
legend(['n = 1', 'n = 2','n = 3','n = 6','n = 12','sin(x)'])
axis([min(x),max(x),min(np.sin(x))-3,max(np.sin(x))+3])
show()



