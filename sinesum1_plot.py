#sinesum1_plot.py

from matplotlib.pyplot import * # import and plotting
from numpy import *

T = 2.*np.pi 										#setting T-value
n = np.array([1,3,20,200]) 									#setting the n values to run

t = linspace(0,T,100)											#calculating t

test = n.shape[0]
print 'test = ',test

def mk_S(t,n,T):
	S = np.zeros((n.shape[0], t.shape[0]))
	print 'S = ',S

	for j in range(n.shape[0]):
		temp_S = 0
		#print 'temp_S=',temp_S
		print 'j = ',j
		for i in range(n[j]):
			#print 'i+1 = ',i+1
			temp_S += 1./(2*(i+1)-1)*np.sin(2*(2*(i+1)-1)*np.pi*t/T)
			#print 'temp_S add = ',temp_S
		S[j] = 4*temp_S/np.pi
		print 'S =',S
	return S





S= mk_S(t,n,T)

def mk_f(t,T):
	f = np.zeros((t.shape[0]))
	
	for i in range(len(f)):

		if 0<t[i]<T/2:
			f[i] = 1
		elif t[i] == T/2:
			f[i] = 0
		elif T/2<t[i]<T:
			f[i] = -1
	return f


f = mk_f(t,T)

plot(t,S[0],'r')
xlabel('t')
ylabel('f(t) / S(t;n)')
hold('on')
plot(t,S[1],'g')
hold('on')
plot(t,S[2],'y')
hold('on')
plot(t,S[3],'c')
hold('on')
plot(t,f,'b')
#axis([t-0.05,t+0.05,min(S)-5,max(S)+5])
legend(['n = 1', 'n=3','n=20','n=200','f(t)'])
title('sinesum1_plot')
savefig('sinesum1_plot.pdf')
show()


