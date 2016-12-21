#Polynomial.py

class Polynomial:
	def __init__(self, coefficients):
		self.coeff = coefficients
	def __call__(self, x):
		s=0
		for i in range(len(self.coeff)):
			s +=self.coeff[i]*x**i
		return s
	def __add__(self, other):
		# Start with the longest list and add in the other
		if len(self.coeff) >len(other.coeff):
			result_coeff =self.coeff[:]  # copy!
			for i in range(len(other.coeff)):
				result_coeff[i] += other.coeff[i]
		else:
			result_coeff = other.coeff[:] # copy!
			for i in range(len(self.coeff)):
				result_coeff[i] +=self.coeff[i]
		return Polynomial(result_coeff)

	def diff(self):
		poly = self.coeff
		for i in range(1,len(poly)):
			poly[i-1] = poly[i]*i
		del poly[-1]
		return Polynomial(poly)


		# l = []

		# for i in range(len(self.coeff)-1):
		# 	l.append(self.coeff[i+1]*(i+1))

		# return Polynomial(l)
		# for i in range(len(self.coeff)):
		# 	self.coeff[i] = self.coeff[i]*(i)
		# del self.coeff[0]
		# return self.coeff
	# def diff(self):
	# 	l =[]
	# 	for i in range(len(self.coeff)-1):
	# 		l.append(self.coeff[i+1]*(i+1))
	# 		self.coeff = l
	# 	return self.coeff