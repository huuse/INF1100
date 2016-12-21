#water_wave_velocity.py

from matplotlib.pyplot import * # import and plotting
from numpy import *


g = 9.81 			# acceleration of gravity
s = 7.9*10**(-2)	#air-water surface tension (N/m)
rho = 1000			#density of water (kg/m**3)
h = 50				#water dept (m)

def mk_c(g,s,rho,h,l):
	return [np.sqrt(g*l/(2*np.pi)*(1+s*4*np.pi**(2)/(rho*g*l**
		(2))*np.tanh(2*np.pi*h/(l)))) for l in l]

l1 = np.linspace(0.001,0.1,50)
l2 = np.linspace(1,2000,50)
print l1
print l2

c1 = mk_c(g,s,rho,h,l1)
c2 = mk_c(g,s,rho,h,l2)
print 'min = ',min(min(c1),min(c2))
figure('small_range')
plot(l1,c1,'bo')
xlabel('Lambda')
ylabel('Wave speed')
title('water_wave_velocity.py(small_range)')

figure('large_range')
plot(l2,c2,'ro')
xlabel('Lambda')
ylabel('Wave speed')
title('water_wave_velocity.py(large_range)')
#savefig('water_wave_velocity(large_range).pdf')
show()
