#piazzatest.py

import numpy as np

n = 10
v=1.
g = 9.81
t = np.linspace(0,2*v/g,n+1)
print int(len(t))
y = v*t -0.5*g*t**2


a =np.zeros((len(t),2))
for i in range(len(t)):
	a[i][0] = t[i]
	a[i][1] = y[i]
print 'a = \n',type(a)

table = [[t,y] for t,y in zip(t,y)]
print type(table)
e=5
print '\n\n',a[e],table[e]

table2 = np.zeros((a.shape[1],a.shape[0]))
for i in range((a.shape[0])):
	table2[0][i] = table[i][0]
	table2[1][i] = table[i][1]
print 'table2 = \n',table2
print 'table = \n',table
print len(table)

print 'a = \n',a
print len(a[5])

q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

print q[0][0], q[1], q[2][-1], q[1][0]

for i in q:
	for j in range(len(i)):
		print i[j]

lst =[]
a=5
b=15
n=10
h = (b-a)/n
for i in range(n+1):
	lst.append(a+i*h)
print 'lst = \n',lst

lst2 = [[a+i*h,'hei %.f'%(n-i)] for i in range(n+1)]
print 'lst2 = \n',lst2

print lst2[2][0]

infile = open('Fdeg.dat','r')
infile.readline()
infile.readline()
infile.readline()
f = []
c = []

for line in infile:
	print 'line = \n', line
	words = line.split()
	f.append(float(words[2]))
[c.append((f[i]-32)*5/9) for i in range(len(f))]


infile.close()

print 'f = \n',f
print 'c = \n',c

outfile = open('f_c_def.dat','w')
outfile.write('fdegrees       cdegrees\n')
print 'fdegrees       cdegrees\n'
outfile.write('-----------------------\n')
print '-----------------------\n'
outfile.write('\n')
for f,c in zip(f,c):
	outfile.write('%6.2f          %6.2f \n' %(f,c))
	print '%6.2f          %6.2f \n' %(f,c)
outfile.close()



