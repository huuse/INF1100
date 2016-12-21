#gaussian2.py
import numpy as np
import math

def gauss(x, m, s):

	f = (1.0/(np.sqrt(2*math.pi)*s))*math.exp(-0.5*((x-m)/(s))**2)
	return f 						#returning f(x) calculated according to the excercise

n = 5 								#choosing number of x-values
m = 0
s = 1.0
xmin = m-5*s 						#creating the max/min xvalues according to the excercise
xmax = m+5*s
gap = (xmax-xmin)/(n-1) 			#calculating the gap size between the x-es
table1 = [] 						#defining the table to fill with the f-values
x = xmin
for i in range(0,n): 				#for loop going through n-values

	table1.append(gauss(x,m,s))		#calling for the function
	x += gap						#updating x-value for nest step

print table1


➜  Progging  python gaussian2.py
[1.4867195147342977e-06, 0.01752830049356854, 0.3989422804014327, 0.01752830049356854, 1.4867195147342977e-06]
