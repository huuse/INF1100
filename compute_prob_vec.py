 7ygv#compute_prob_vec.py

import random
import numpy as np
import time


t0 = time.time()
#i = 1,2,3,6
i = 6

N=10
r=np.random.rand(N**i)

result = float(sum(np.logical_and(0.5<=r,r<=0.6)))/(N**i)

print 'i= ',i
print result

t1 = time.time()

total = t1-t0
print 'time= ',total



"""
The vectorial version of the code is slower than the scalar one. What am I doing wrong?

python compute_prob_vec.py
i=  1
0.1
time=  0.00188899040222

python compute_prob_vec.py
i=  2
0.11
time=  0.000879049301147

python compute_prob_vec.py
i=  3
0.098
time=  0.0022349357605

python compute_prob_vec.py
i=  6
0.09982
time=  2.0408217907



"""


