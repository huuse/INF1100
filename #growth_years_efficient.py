#growth_years_efficient.py

#from scitools.std import *
from numpy import *
x0 = 100
p = 5
N = 4
# initial amount
# interest rate
# number of years
index_set = range(N+1)
x = zeros(len(index_set))
# Compute solution
x[0] = x0
for n in index_set[1:]:
    x[n] = x[n-1] + (p/100.0)*x[n-1]
print x
plot(index_set, x, 'ro', xlabel='years', ylabel='amount')