#area_triangle.py
#import numpy as np
#import cmath

def area(a):
	A = 0.5*(a[1][0]*a[2][1] - a[2][0]*a[1][1] - a[0][0]*a[2][1] + a[2][0]*a[0][1] + a[0][0]*a[1][1] - a[1][0]*a[0][1])
	print 
	return A 										#calculating A and returning it in the function 'area'






v1 = [0,0]; v2 = [1,0]; v3 = [0,2] 					#defining the vertices
certices = [v1,v2,v3] 								#putting the vertices in a list
triangle1 = area(certices) 							#calling for the function
print 'Area of triangle is %.2f' % triangle1

"""
Progging  python area_triangle.py
Area of triangle is 1.00
"""


