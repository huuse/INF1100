#compare_floats.py

a = 1/947.0*947
b = 1
tol = 10**(-15.9545897)
if abs(a - b) > tol:
	print 'Wrong results!'

else:
	print 'Correct results!'
