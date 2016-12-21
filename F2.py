#F2.py


from math import exp, sin

class F2:
	def __init__(self, a, w):
		self.a = a
		self.w = w

	def __str__(self):
		return 'exp(-a*x)*sin(w*x)'

	def value(self,x):

		return exp(-self.a*x)*sin(self.w*x)



# from F2 import F2
# f = F2(a=1.0, w=0.1)
# from math import pi

# print f.value(x=pi)
# f.a = 2
# print f.value(pi)

# print f

# """
# python F2.py
# 0.013353835137
# 0.00057707154012
# exp(-a*x)*sin(w*x)
# 0.013353835137
# 0.00057707154012
# exp(-a*x)*sin(w*x)
# """