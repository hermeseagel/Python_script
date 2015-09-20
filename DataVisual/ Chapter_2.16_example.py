import matplotlib.pylab as pylab
#from pylab import *
import numpy as np
def moving_average(interval, window_size):
	window = np.ones(int(window_size) / float(window_size))
	return pylab.convolve(interval, window, 'same')
t = np.linspace(-4, 4, 100)
y = np.sin(t) + np.random.randn(len(t))*0.1
pylab.plot(t, y, "k.")
y_av= moving_average(y,10)
pylab.plot(t, y_av, "r")
pylab.xlabel("Time")
pylab.ylabel("Value")
pylab.grid(True)
pylab.show()