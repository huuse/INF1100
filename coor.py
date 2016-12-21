#coor.py
from tabulate import tabulate

aa = []					#creating collum 1 in the matrix
bb = []					#creating collum 2 in the matrix
b = 20. 				#defining constants
a = 10					#defining constants
n = 10 					#defining constants
h = 0					#defining constants


for i in range(0,n+1):

	h += (b-a)/n
	xi = a + i*h
	aa.append(xi)
	bb.append(h)


coor = []
coor.append(aa)
coor.append(bb)
print coor
print "coor = "
print coor[0 ][2]
coor2 = map(list, zip(*coor))

print coor2

####################### b #################
h = (b-a)/n
aaa = [a + i*h for i in range(n+1)]
bbb = [(b-a)/n*i for i in range(n+1)]

coor3 = []

coor3.append(aaa)
coor3.append(bbb)
coor4 = map(list, zip(*coor3))
print coor4[1][0]


################## from chapter 2 testes #################
C = [-10, -5, 0, 5, 10, 15, 20, 25]
C.insert(3,3)
print C
print 10 in C
print C.index(10)
somelist = [1,2,3]
a, b, c = somelist
print b


degrees = [0, 10, 20, 40, 100]
C = [1,2,3]

print 'C lookes like this: ', C
for D in degrees:
	print 'list element:', D
print 'The degrees list has', len(degrees), 'elements'


