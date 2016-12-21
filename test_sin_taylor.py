#test_sin_taylor.py

import numpy as np

#a)
"""
a[j] = -x**2/((2*j+1)*2*j)*a[j-1]
s[j] = s[j-1]+a[j-1]
"""
#b)

def sin_Taylor(x,n):
    a = np.zeros(n+2)
    s = np.zeros(n+2)

    a[0] = x
    #s[0] = 0

    for j in range(1,n+2):
        a[j] = -x**2/((2*j+1)*2*j)*a[j-1]
        s[j] = s[j-1]+a[j-1]

    return s[n+1], abs(a[n+1])

print "b:"
n = 10
result = sin_Taylor(np.pi/2,n)
print "With polynomial order %g, sin(pi/2) = %g, error = %g." %(n,result[0], result[1])



#c)
"""
n = 2
S = x - (x**3)/3! + (x**5)/5!
"""
from math import factorial

def test_sin_Taylor():
    n = 2
    x = 3*np.pi/2
    tol = 1e-10
    
    expected = x - (x**3)/factorial(3) + (x**5)/factorial(5)
    computed = sin_Taylor(x,n)[0]
    success = abs(expected-computed) < tol

    assert success

print "c:"
test_sin_Taylor()

#d)

print "d:"
x_values = [0.25*np.pi,0.5*np.pi,np.pi]
n_values = [1, 5,10]

print "%10s %10s %10s %10s" %('x-value', 'order', 'approx', 'exact')
for x in x_values:
    for n in n_values:
        print "%10f  %10d %10f %10f" %(x,n,sin_Taylor(x,n)[0], np.sin(x))