#test_fill_arrays_vectorized.py


import numpy as np

x = np.linspace(-4,4,41)
print x
h = [1/(np.sqrt(2*np.pi))*np.e**(-0.5*X**(2)) for X in x]

print 'x = ',x
print 'h = ',h