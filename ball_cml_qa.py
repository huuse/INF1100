#ball_cml_qa.py
import sys

try: 										#Testing if a valued imput for "t" is given from the command line

	t = float(sys.argv[1])
except: 									#If not, a new input is requested
	t = float(raw_input('Give t:'))



try:										#Testing if a valued imput for "v0" is given from the command line

	v0 = float(sys.argv[2])
except:  									#If not, a new input is requested
	v0 = float(raw_input('Give v0:'))



g = 9.81
y = v0*t - 0.5*g*t**2



print y




"""
Progging python ball_cml_qa.py
Give t:0.6
Give v0:3
0.0342

Progging python ball_cml_qa.py 0.6 kljlk
Give v0:3
0.0342


python ball_cml_qa.py kj 3
Give t:3
-35.145
"""
