#f2c_approx_table.py
from tabulate import tabulate
tempf = []
#tempf.insert(0, 'F')
tempc = []
#tempc.insert(0, 'C')

tempcap = []
#tempcap.insert(0, '~C')


for i in range(0,11):

	tempf.insert(i, i*10)
	C = i*10.0*5/9 -32*5/9

	tempc.insert(i, C)
	tempcap.insert(i, (i*10.0-30)/2)

print 'tempf = ', tempf
print 'tempc = ', tempc
print 'tempcap = ', tempcap


temp = zip(tempf,tempc,tempcap)

print temp[0][1]


print tabulate(temp, headers = ["F", "C", "~C"], floatfmt=".2f")


Progging  python f2c_approx_table.py
tempf =  [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
tempc =  [-17.0, -11.444444444444445, -5.888888888888889, -0.33333333333333215, 5.222222222222221, 10.777777777777779, 16.333333333333336, 21.888888888888886, 27.444444444444443, 33.0, 38.55555555555556]
tempcap =  [-15.0, -10.0, -5.0, 0.0, 5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0]
-17.0
  F       C      ~C
---  ------  ------
  0  -17.00  -15.00
 10  -11.44  -10.00
 20   -5.89   -5.00
 30   -0.33    0.00
 40    5.22    5.00
 50   10.78   10.00
 60   16.33   15.00
 70   21.89   20.00
 80   27.44   25.00
 90   33.00   30.00
100   38.56   35.00



