#kick.py

#!/usr/bin/python
import math
import numpy as np


g = 9.81		#m/s**2
q = 1.2			#kg/m**3
a = 0.11		#m (ball radius)
m = 0.43 		#kg (mass of ball)
CD = 0.2		#drag coefficient
#Vh = 120/3.6	#m/s (hard kick)
#Vs = 10/3.6 	#km/h (soft kick)
V = np.array([120/3.6, 10/3.6])
G = m*g

print V
A = math.pi*a**2
Fd = 0.5*CD*q*A*V**2
#Fdh = 0.5*CD*q*A*Vh**2

#Fds = 0.5*CD*q*A*Vs**2

#Rh = Fdh/G		#drag force/gravity ratio (hard kick)
#Rs = Fds/G 		#drag force/gravity ratio (soft kick)
R = Fd/G
print R
print "hard kick = %.1f N" %Fd[0]
print "soft kick = %.1f N" %Fd[1]
print "gravity force = %.1f N" %G
print "ratio hard kick = %g" %R[0]
print "ratio hard kick = %g" %R[1]
