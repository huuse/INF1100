#midttermin2015.py
"""
import sys
a = sys.argv[1]
b = sys.argv[2]
print a+b
print eval(a)+eval(b)
"""

"""
from numpy import *

x = linspace(0,3,3)
print x
"""

""""
A = ['5', '6', '7', 'end']
try:
    b = float(A[3])
except IndexError:
    print 'A has length %d' %len(A)
except ValueError:
    print 'Cannot convert "%s" to float'% A[3]

print '%1.2f' %b
"""

"""
def f(x):
    return x + 2
def test_f():
    x = 1.0
    expected = 3.0
    computed = f(x)

    tol = 1E-14
success = abs(exact-computed) < tol
msg = 'expected %g, computed %g' %(expected,computed)
assert success, msg
"""

import numpy as np
import sys

def func_deriv(x):
	F = np.sin(a*np.pi*x)

	f = a*np.pi*np.cos(a*np.pi*x)

	return F,f
try:
	a = float(sys.argv[1])
except IndexError:
	print 'Error. No value given for "a".'
	sys.exit(1)
except ValueError:
	print 'Error. The value for "a" needs to be a float.'
	sys.exit(1)
F,f=func_deriv(7)


print 'F = %f and f = %f' %(F,f)
print 'F = ',F


