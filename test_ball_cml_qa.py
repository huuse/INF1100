#test_ball_cml_qa.py
import sys

try:
	v0 = float(sys.argv[1])
except 
	t = float(sys.argv[2])

except IndexError:
	v0 = float(raw_input('give v0: '))
	t = float(raw_input('give t: '))

g = 9.81
y = v0*t - 0.5*g*t**2

print y