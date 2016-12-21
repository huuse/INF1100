#plot_test.py

from matplotlib.pyplot import * # import and plotting
from numpy import *


# Make points along the curve

t = np.linspace(0, 3, 51) # 50 intervals in [0, 3]
y = t**2*np.exp(-t**2)



plot(t, y)
savefig('fig.pdf')
savefig('fig.png')
show()
