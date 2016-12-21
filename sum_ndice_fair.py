#sum_ndice_fair.py


import sys
import numpy as np
import itertools


try:

	s = int(sys.argv[1])
except:  									
	s = int(raw_input('Give "s", the sum limit: '))

try:

	n = int(sys.argv[2])
except:  									
	n = int(raw_input('Give "n", number of dices: '))
	

N=1000000
cost = -1
count = 0
fair = 1e-3

def mk_game(n,s):
	throw = np.random.randint(1,7,n)
	success = np.sum(throw)<s
	return success
	



sum_success = np.sum([mk_game(n,s) for i in range(N)])
p = float(sum_success)/(N)


print 'the revard should be, abs(cost)/p = ',abs(cost)/p

	
"""
python sum_ndice_fair.py 9 4  
the revard should be, abs(cost)/p =  18.514746996

running exercise 8.8 with this r gave: 
python sum_4dice.py 18.514746996 1000000
money=  3536.31667719 


"""
	

