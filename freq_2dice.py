#freq_2dice.py

import numpy as np

N = 10000

throw = np.random.randint(1,7,N*2).reshape(N,2)
sums = np.sum(throw,axis=1)

value, appear = np.unique(sums, return_counts=True)
m = np.asarray((value, appear)).T

stat = appear/float(N)


#exaxt values:
perm = np.zeros((6,6))
dice1 = np.arange(1,7)
dice2 = dice1
for i in dice1:
	for j in dice2:
		perm[i-1][j-1]=dice1[i-1]+dice2[j-1]

valueex, appearex = np.unique(perm, return_counts=True)
mex = np.asarray((valueex,appearex)).T
statex = appearex/36.0

values = np.arange(2,13)#.reshape(11,1)
print '-dice value- -exaxt propability- -estimated propability-:\n'\
		, np.asarray((values, statex,stat)).T



"""
python freq_2dice.py
-dice value- -exaxt propability- -estimated propability-:
[[  2.           0.02777778   0.027     ]
 [  3.           0.05555556   0.0536    ]
 [  4.           0.08333333   0.0845    ]
 [  5.           0.11111111   0.1104    ]
 [  6.           0.13888889   0.1384    ]
 [  7.           0.16666667   0.1708    ]
 [  8.           0.13888889   0.1413    ]
 [  9.           0.11111111   0.111     ]
 [ 10.           0.08333333   0.0804    ]
 [ 11.           0.05555556   0.0534    ]
 [ 12.           0.02777778   0.0292    ]]
 """
