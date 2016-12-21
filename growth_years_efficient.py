#growth_years_efficient.py


from numpy import *




outfile = open('growth_years_efficient.dat','w')
outfile.write('growth_years_efficient\n\n')
outfile.write('n 	x\n')
outfile.write('-----------\n')
N = 4
x0 = 100
p = 5
count = 0
outfile.write('%d 	%.2f \n' %(count,x0))
while count < N:
	
	x = (1+p/100.0)*x0
	count += 1
	outfile.write('%d 	%.2f \n' %(count,x))
	x0 = x
outfile.close()



