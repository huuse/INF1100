#f2c_shortcut_plot.py



from matplotlib.pyplot import * # import and plotting
from numpy import *



def mk_Ccirca(Fdegrees):
	return [(F-30)/2. for F in Fdegrees]

def mk_Cexact(Fdegrees):
	return [(F-32)*5/9. for F in Fdegrees]

Fdegrees = np.arange(-20,121)
Ccirca = mk_Ccirca(Fdegrees)
Cexact = mk_Cexact(Fdegrees)



plot(Fdegrees,Ccirca,'-r')
hold('on')
plot(Fdegrees, Cexact, 'bo')
xlabel('Fahrenheit')
ylabel('Celcius degrees')
legend(['Circa relation', 'Exact relation'])
savefig('f2c_shortcut_plot.pdf')
show()

