#ball_cml.py
import sys

t = float(sys.argv[1]) 				#Getting parameter "t" from the command line

v0 = float(sys.argv[2]) 			#Getting parameter "v0" from the command line

g = 9.81
y = v0*t - 0.5*g*t**2

print y

"""
Progging python ball_cml.py 0.6 3
0.0342
"""
