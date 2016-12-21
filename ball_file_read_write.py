#ball_file_read_write.py
import numpy as np
import os
os.system('cls' if os.name == 'nt' else 'clear') 	#clear the terminal
import csv
import random
from itertools import permutations
import sys
#4-14.dat




def mk_file_reader(textfile):
	infile = open('tvalues.dat', 'r')

	t = []

	infile.readline()
	v = infile.readline()
	v = v.split()
	v0 = float(v[1])

	infile.readline()
	for line in infile:

		l = line.split()
		for i in range(0,len(l)):
			t.append(round(float(l[i]),8))
	infile.close()

	return v0, t







##########################		a)		#########################
"""
v0, t = mk_file_reader('tvalues.dat')
print 'v0=\n',v0
print 't=\n',t

"""

"""
v0=
3.0
t=
[0.15592, 0.28075, 0.36807889, 0.35, 0.57681502, 0.21342619, 0.0519085, 0.042, 0.27, 0.50620017, 0.528, 0.2094294, 0.1117, 0.53012, 0.372985, 0.39325246, 0.21385894, 0.3464815, 0.57982969, 0.10262264, 0.29584013, 0.17383923]
"""
##########################		a)	done	#########################


##########################		b)		#########################
def mk_outfile_t_y():
	v0, t = mk_file_reader('tvalues.dat')
	t = sorted(t)
	print 'tsorted = \n',t
	outfile = open('outfile414b.dat','w')
	g = 9.81
	outfile.write('t values    y values\n')
	outfile.write('------------------------\n')
	t = np.array(t)
	temp = v0*t-0.5*g*t**2
	for i in range(0,len(t)):
		outfile.write("%f    %f \n" % (t[i], temp[i]))

	outfile.close()


k = mk_outfile_t_y()


"""
tsorted =
[0.042, 0.0519085, 0.10262264, 0.1117, 0.15592, 0.17383923, 0.2094294, 0.21342619, 0.21385894, 0.27, 0.28075, 0.29584013, 0.3464815, 0.35, 0.36807889, 0.372985, 0.39325246, 0.50620017, 0.528, 0.53012, 0.57681502, 0.57982969]

t values    y values
------------------------
0.042000    0.117348
0.051909    0.142509
0.102623    0.256211
0.111700    0.273901
0.155920    0.348514
0.173839    0.373288
0.209429    0.413152
0.213426    0.416852
0.213859    0.417243
0.270000    0.452425
0.280750    0.455635
0.295840    0.458228
0.346481    0.450602
0.350000    0.449137
0.368079    0.439697
0.372985    0.436582
0.393252    0.421211
0.506200    0.261750
0.528000    0.216564
0.530120    0.211922
0.576815    0.098475
0.579830    0.090416
"""
##########################		b) done		#########################


##########################		c)		#########################

def test_414c(inputfile):
	inputfile = open(inputfile)
	test1,test2 = mk_file_reader(inputfile)

	if test1 == 3.0 and type(test2) ==list and len(test2)==22:
		print 'ok'
		return 'sucsess. The code is working ok.'

	else:
		print 'fail'
		return 'Fail. The code is NOT working ok.'
	inputfile.close()
r = test_414c("tvalues.dat")
"""
print r
"""
"""
ok
sucsess. The code is working ok.
"""

##########################		c) done		#########################


