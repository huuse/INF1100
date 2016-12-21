#one6_ndice.py
import sys
import numpy as np

try:

	n = int(sys.argv[1])
except:  									
	n = int(raw_input('Give "n", number of dice to throw: '))


try:

	ne = int(sys.argv[2])
except:  									
	ne = int(raw_input('Give "ne", number of experiments to run: '))



throw = np.random.randint(1,7,ne*n).reshape(ne,n)
how_many_6 = 0
for rows in throw:
	if np.any(rows == 6):

		how_many_6 += 1

print float(how_many_6)/(ne)

"""
python one6_ndice.py 2 1   
0.0

python one6_ndice.py 2 10
0.2

python one6_ndice.py 2 100 
0.32

python one6_ndice.py 2 1000
0.304

"""