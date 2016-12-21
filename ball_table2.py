#ball_table2.py

from tabulate import tabulate

n = 9
v0 = 10
g = 9.81
#stepsize = math.floor(2*v0/g*1/(n+1))

t = []
y = []

for i in range(1,n+1,1):
	tval = (2*v0/g/n)*(i-1)
	yval = v0*tval - 0.5*g*tval**2

	t.append(tval)
	y.append(yval)




#print("%.2f" %t)
#print("%.2f" %y)
list1 = zip(t,y)

print tabulate(list1, headers = ["Time", "y"])

➜  Progging  python ball_table2.py
    Time        y
--------  -------
0         0
0.226526  2.01357
0.453052  3.52374
0.679579  4.53052
0.906105  5.03392
1.13263   5.03392
1.35916   4.53052
1.58568   3.52374
1.81221   2.01357




