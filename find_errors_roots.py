#find_errors_roots.py


a = 2; b = 4; c = 1
from math import sqrt
q = b*b - 4*a*c
print q
q_sr = sqrt(q)
x1 = (-b + q_sr)/(2*a)
x2 = (-b - q_sr)/(2*a)
print x1, x2
