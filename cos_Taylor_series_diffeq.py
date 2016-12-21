#cos_Taylor_series_diffeq.py


import numpy as np

#a)
"""
a[j] = -x**(2)/(2.*j*(2*j-1))*a[j-1]
s[j] = s[j-1]+a[j-1]
"""
#b)

def cos_Taylor(x,n):
    a = np.zeros(n+2)
    s = np.zeros(n+2)

    a[0] = 1
    #s[0] = 0

    for j in range(1,n+2):
        a[j] = -x**(2)/(2*j*(2*j-1))*a[j-1]
        #*2*np.pi/360
        s[j] = s[j-1]+a[j-1]

    return s[n+1], abs(a[n+1])

print "b:"
n = 10
result = cos_Taylor(np.pi/2,n)
print "With polynomial order %g, cos(pi/2) = %g, error = %g." %(n,result[0], result[1])



#c)
"""
n = 2
S = 1 - (x**2)/2! + (x**4)/4!
"""
from math import factorial

def test_cos_Taylor():
    n = 2
    x = 3*np.pi/2
    tol = 1e-10
    expected = 1. - (x**2)/factorial(2) + (x**4)/factorial(4)
    computed = cos_Taylor(x,n)[0]
    success = abs(expected-computed) < tol


    assert success

print "c:"
test_cos_Taylor()

#d)

print "d:"
x_values = [0.25*np.pi,0.5*np.pi,np.pi]
n_values = [1, 5,10]


print "%10s %10s %10s %10s" %('x-value', 'order', 'approx', 'exact')
for x in x_values:
    for n in n_values:
        print "%10f  %10d %10f %10f" %(x,n,cos_Taylor(x,n)[0], np.cos(x))


