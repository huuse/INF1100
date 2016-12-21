#test.readfile.py

import numpy


infile = open('tvalues.dat', 'r')

t = []

infile.readline()
v0 = infile.readline()
print v0

infile.readline()
for line in infile:

	l = line.split()
	print 'l=',l
	for i in range(0,len(l)):
		print 'i=',i
		t.append(round(float(l[i]),8))

print 't = \n',t

"""
infile.readline()
temp = split(1)
v0 = float(temp[1])
print v0
for line in infile:
	ts = line.split()
	t.append(ts)
print infile.read()

"""
infile.close()
