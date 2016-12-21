#Heaviside.py


def H(x):  							# creating the H-function

	if x < 0:
		return 0
	elif x>= 0 :
		return 1



def test_H():

	print 'For x = -10, Heaviside should return 0. H(-10) = %d' %H(-10)
	print 'For x = -10^(-15), Heaviside should return 0. H(-10**(-15)) = %d' %H(-10**(-15))
	print 'For x = 0, Heaviside should return 1. H(0) = %d' %H(0)
	print 'For x = 10, Heaviside should return 1. H(10) = %d' %H(10)


test_H()



➜  Progging  python Heaviside.py
For x = -10, Heaviside should return 0. H(-10) = 0
For x = -10^(-15), Heaviside should return 0. H(-10**(-15)) = 0
For x = 0, Heaviside should return 1. H(0) = 1
For x = 10, Heaviside should return 1. H(10) = 1
