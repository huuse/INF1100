#fortune_and_inflation1.py

import numpy as np
from matplotlib.pyplot import *

P = 5. 				#interest in percent
N = 20				#number of years to calculate
F = 1000000. 			#fortune
I = 2.32 			#inflation in percent
q = 80.				#percent of interest to consume

x0 = F 				#first fortune
c0 = P*q*F/10**4	#what to consume

F_list = np.zeros(N+1)
F_list[0] = F
for i in range(1,N+1):
	F_list[i] =  x0 +P/100.*x0 -c0
	c0 = c0+I/100.*c0
	x0 = F_list[i]

figure('fortune_and_inflation1')
plot(range(N+1),F_list)
title('fortune_and_inflation1')
xlabel('years')
ylabel('fortune')
show()
