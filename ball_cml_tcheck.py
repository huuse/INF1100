#ball_cml_tcheck.py

import sys

t = float(sys.argv[1]) 							#Getting parameter "t" from the command line

v0 = float(sys.argv[2]) 						#Getting parameter "v0" from the command line

g = 9.81
y = v0*t - 0.5*g*t**2

if 0<t<2*v0/g: 									#Checking it the value set for "t" is ok

	print y

else: 											#If not, message is printed and the system exits the program
	print 'Value for t not valid'

	sys.exit(1)  # abort



"""
Progging python ball_cml_tcheck.py 0.6 3
0.0342

Progging python ball_cml_tcheck.py 3 3
Value for t not valid
"""
