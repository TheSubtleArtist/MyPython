import matplotlib_inline as main
from scipy import signal
import numpy as np
import matplotlib.pyplot as plot


t = np.linspace(0,2,4000)
t2 = np.linspace(-1,1,2 * 100)
t3 = np.linspace(0,10,501)



if __name__ == '__main__':
    signal_space= 3 * np.pi * 3 * t
    plot.plot(t, signal.sawtooth(signal_space))
    plot.ylim(-2,2)
    plot.title('Satooth Signal')
    plot.show()

    plot.plot(t,signal.square(signal_space))
    plot.ylim(-2,2)
    plot.title('Square Signal')
    plot.show()


    signal_space2 = 2* np.pi * t
    sig = np.sin(signal_space2)
    pwm = signal.square(30 * signal_space2, duty = (sig +1)/2)

    plot.subplots_adjust(wspace=0.5,hspace=0.5)

    plot.subplot(2,1,1)
    plot.plot(t, sig)
    plot.ylim(-1.5,1.5)
    plot.title('Sine Wave')
    plot.subplot(2,1,2)
    plot.plot(t,pwm)
    plot.ylim(-1.5,1.5)
    plot.title('PWM Wave')
    plot.show


    i,q,e = signal.gausspulse(t2, fc=4, retquad=True, retenv=True)
    plot.plot(t2,i, '-')
    plot.plot(t2,q,'--')
    plot.plot(t2,e,'-.')
    plot.show()

    w = signal.chirp(t3, f0=10, f1=0.1, t1=20, method='linear')
    plot.plot(t3,w)
    plot.title('Linear Chirp')
    plot.xlabel('t (sec)')
    plot.show()




