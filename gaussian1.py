#gaussian1.py
#!/usr/bin/python
import math

m = 0
s = 2.0
x = 1
pi = math.pi
f = 1/(math.sqrt(2*pi)*s)*math.exp(-0.5*((x-m)/(s))**2)
#f = math.exp(1)
print f

➜  Progging  python gaussian1.py
0.176032663382
