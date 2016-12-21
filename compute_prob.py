#compute_prob.py

import random
import time
t0 = time.time()
N = 10
#i = 1,2,3,6
i = 6
def mk_probability(N):
	M = float(0)
	for n in range(N):
		r = random.uniform(0,1)
		if 0.5<=r and r<=0.6:
			M +=1
	return float(M/N)


prob = mk_probability(N**i)
print 'i=',i
print prob	
t1 = time.time()

total = t1-t0
print 'time= ',total



"""
python compute_prob.py
i= 1
0.1
time= 0.000464916229248

python compute_prob.py
i= 2
0.08
time= 0.000219106674194

python compute_prob.py
i= 3
0.106
time= 0.000975131988525


python compute_prob.py    
i= 6
0.100229
time= 1.22528409958


"""