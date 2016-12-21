#read_error.py


def L(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    return s

def L2(x, n):
    s = 0
    for i in range(1, n+1):
        s += (1.0/i)*(x/(1.0+x))**i
    value_of_sum = s
    first_neglected_term = (1.0/(n+1))*(x/(1.0+x))**(n+1)
    from math import log
    exact_error = log(1+x) - value_of_sum
    return value_of_sum, first_neglected_term, exact_error


def table(x):
    from math import log
    print '\nx=%g, ln(1+x)=%g' % (x, log(1+x))
    for n in [1, 2, 10, 100, 500]:
        value, next, error = L2(x, n)
        print 'n=%-4d %-10g  (next term: %8.2e  '\
              'error: %8.2e)' % (n, value, next, error)

table(10)
table(100)
table(1000)

def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i



########################## 		Exercise 6.4 		###################

def table2(x):

    from math import log
    outfile = open('read_error.dat','w')
    outfile.write('read_error.py data file\n\n')
	
    for k in range(4, 14, 2):
        epsilon = 10**(-k)
        approx, n = L3(x, epsilon=epsilon)
        exact = log(1+x)
        exact_error = exact - approx
        outfile.write('epsilon: %5.0e, exact error: %8.2e, n=%d \n' % \
              (epsilon, exact_error, n))
        print 'epsilon: %5.0e, exact error: %8.2e, n=%d' % \
              (epsilon, exact_error, n)

print '\n\n'
table2(10)




def mk_read_error(filename):
	infile = open(filename,'r')
	infile.readline()
	infile.readline()
	epsilon = []
	error = []
	n =[]
	epsilon_start = 9
	error_start = 29
	n_start = 41
	for line in infile:
		epsilon.append(float(line[epsilon_start:epsilon_start+5]))
		error.append(float(line[error_start:error_start+8]))
		n.append(int(line[n_start:line.find('')-1]))

	return epsilon,error,n

epsilon,error,n = mk_read_error('read_error.dat')

from matplotlib.pyplot import *


semilogy(n, epsilon)
title('read_error plot')
xlabel('n')
ylabel('log epsilon/exact error')
grid(True)
hold('on')
semilogy(n,error)
legend(['epsilon','exact error'])
show()














