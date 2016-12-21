#ball_table3.py


from tabulate import tabulate

n = 9
v0 = 10
g = 9.81

t = []
y = []

for i in range(n+1):
	tval = (2*v0/g/n)*(i)
	yval = v0*tval - 0.5*g*tval**2

	t.append(tval)
	y.append(yval)




ty1 = []
ty1.append(t)
ty1.append(y)

print "\n ty1: \n"
for i in range(n+1):
	print("%.2g %.2g" %(ty1[0][i], ty1[1][i])) 		#a)


ty2 = map(list, zip(*ty1))
print '\n ty2 : \n'
for i in range(n+1):

	print "%.2g %.2g " %(ty2[i][0], ty2[i][1])


➜  Progging  python ball_table3.py

 ty1:

0 0
0.23 2
0.45 3.5
0.68 4.5
0.91 5
1.1 5
1.4 4.5
1.6 3.5
1.8 2
2 0

 ty2 :

0 0
0.23 2
0.45 3.5
0.68 4.5
0.91 5
1.1 5
1.4 4.5
1.6 3.5
1.8 2
2 0
