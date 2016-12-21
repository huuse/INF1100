#roots_quadratic.py
import numpy as np 							#importing numpy package
import cmath
def roots(a,b,c):							#defining the function



	r1 = (-b+np.sqrt(b**2.0-4*a*c))/(2*a)	#calculating the two roots
	r2 = (-b-np.sqrt(b**2.0-4*a*c))/(2*a)

	return r1, r2 							#returning the two roots






def test_roots_float(a,b,c):

	rf1,rf2 = roots(a,b,c)
	#if isinstance(rf1,float) == True and isinstance(rf2,float) == True:
	if cmath.isnan(rf1) == False and cmath.isnan(rf2) == False:
		return 'root 1 and 2 is real' ,rf1,rf2
	else:
		return 'float wrong'

def test_roots_complex(a,b,c):

	rc1,rc2=roots(a,b,c)
	if cmath.isnan(rc1) == True and cmath.isnan(rc2) == True:
		return 'root 1 and 2 is complex'
	else:
		return 'error', rc1,rc2



print 'test for float values: a=1, b=3 and c=1:' ,test_roots_float(1,3,1)

print 'test for complex values: a=2, b=4 and c=10:' ,test_roots_complex(2,4,10)

➜  Progging  python roots_quadratic.py
test for float values: a=1, b=3 and c=1: ('root 1 and 2 is real', -0.3819660112501051, -2.6180339887498949)
roots_quadratic.py:8: RuntimeWarning: invalid value encountered in sqrt
  r1 = (-b+np.sqrt(b**2.0-4*a*c))/(2*a)	#calculating the two roots
roots_quadratic.py:9: RuntimeWarning: invalid value encountered in sqrt
  r2 = (-b-np.sqrt(b**2.0-4*a*c))/(2*a)
test for complex values: a=2, b=4 and c=10: root 1 and 2 is complex

