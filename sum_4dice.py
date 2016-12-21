#sum_4dice.py


import sys
import numpy as np
import matplotlib.pyplot as pl

try:

	r = float(sys.argv[1])
except:  									
	r = float(raw_input('Give "r", the reward: '))


try:

	n = int(sys.argv[2])
except:  									
	n = int(raw_input('Give "n", number of experiments to run: '))



throw = np.random.randint(1,7,n*4).reshape(n,4)
sm = np.sum(throw, axis=1)
success = 0
test =np.zeros(n)
ntest= np.arange(0,n)
i=0
for row in sm:
	if row<9:
		success +=1
		test[i] = test[i-1]-1+r
	else:
		test[i]=test[i-1]-1
	i +=1

money = -1*n +r*success
print 'money= ',money
pl.plot(ntest,test)
pl.show()


"""
python sum_4dice.py 10 1 
money=  -1


python sum_4dice.py 10 10
money=  -10


python sum_4dice.py 10 100
money=  10


python sum_4dice.py 10 1000
money=  -440

"""