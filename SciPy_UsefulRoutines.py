from scipy import signal 
from scipy import integrate
from scipy import interpolate
import numpy as np
import matplotlib.pyplot as plot

def showSignal():
    a = b = np.arange(25).reshape((5,5))
    c = d = np.arange(125).reshape((5,5,5))
    signal.convolve2d(a,b)
    signal.correlate2d(a,b)
    signal.convolve(c,d)
    signal.correlate(c,d)

def showIntegrate():
    x3 = lambda x: x**3
    integrate.quad(x3,0,3)

    e = np.arange(9).reshape((3,3))

    integrate.trapezoid(e,axis=0)
    integrate.trapezoid(e,axis=1)
    integrate.trapezoid(e,axis=-1)
    integrate.trapezoid(e,axis=-2)

    integrate.cumulative_trapezoid(e,axis=0)
    integrate.cumulative_trapezoid(e,axis=1)
    integrate.cumulative_trapezoid(e,axis=-1)
    #integrate.cumulative_trapezoid(e,axis=2)
    #integrate.cumulative_trapezoid(e,axis=-2)

    integrate.simpson(e,axis=0)
    integrate.simpson(e,axis=-1)
    integrate.simpson(e,axis=1)

def showInterpolate():
    x = np.linspace(0,10,3)
    y=np.cos(x**1/2+6)
    print(x,y)
    plot.plot(x,y,'o-')
    plot.show()
    f1 = interpolate.interp1d(x,y,kind='linear')
    f2 = interpolate.interp1d(x,y,kind='nearest')
    xnew = np.linspace(0, 10, 30)
    plot.plot(x, y, 'o')
    plot.plot(xnew, f1(xnew), '-')
    plot.plot(xnew, f2(xnew), ':')
    labels=['Original', 'Linear', 'Nearest']
    plot.legend(labels, loc='best')
    plot.show()




if __name__ == '__main__':
    showSignal()
    showIntegrate()
    showInterpolate()



    
    
