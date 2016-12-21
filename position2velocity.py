#position2velocity.py
from matplotlib.pyplot import *
infile = open('position2velocity.dat','r')

s = int(infile.readline())

x = []
y = []
for line in infile:
	word = line.split()

	x.append(float(word[0]))
	y.append(float(word[1]))
infile.close()


#a

plot(x,y)
xlabel('x')
ylabel('y')
title('position2velocity a)')
show()


#b

vx = []
vy = []
t = []
t_temp=0
for k in range(len(x)-1):
	vx.append((x[k+1]-x[k])/s)
	vy.append((y[k+1]-y[k])/s)
	t_temp += k
	t.append(t_temp)

plot(t,vx)
xlabel('t')
ylabel('vx')
title('position2velocity b) 1')
show()

plot(t,vy)
xlabel('t')
ylabel('vy')
title('position2velocity b) 2')
show()


