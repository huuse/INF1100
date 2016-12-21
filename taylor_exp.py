#taylor_exp.py
def taylor_exp(N):
	from math import factorial
	from Polynomial import Polynomial
	l = []
	for k in range(N):
		l.append(1.0/(factorial(k)))
	return Polynomial(l)