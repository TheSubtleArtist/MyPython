import matplotlib_inline as main
import numpy as np
import matplotlib.pyplot as plot

t = np.arange(128)
a=np.mgrid[:3,:3][0]
b=np.mgrid[:3,:3,:3][0]

if __name__ == '__main__':
    sp=np.fft.fft(np.sin(t)) # Compute the one-dimensional discrete Fourier Transform.
    freq=np.fft.fftfreq(t.shape[-1]) # Compute the one-dimensional discrete Fourier Transform.
    print("dp: \n", sp)
    print("freq: \n", freq)

    plot.subplot(2,1,1)
    plot.title('Real Part')
    plot.plot(freq, sp.real)
    plot.subplots_adjust(hspace=0.5)

    plot.subplot(2,1,2)
    plot.title('Imaginary Part')
    plot.plot(freq, sp.imag)
    plot.show()

    print("mgrid(a):\n", a)
    print("2D FFT:\n", np.fft.fft2(a))

    print('mgrid(b):\n', b)
    print("3D FFT:\n", np.fft.fftn(b, axes=(1,2)))
    print("N-Dimensional FFT:\n", np.fft.fftn(b, axes=(0,1)))

    [X,Y] = np.meshgrid( 2 * np.pi * np.arange(200) / 12, 2 * np.pi * np.arange(200) / 34 )
    plot.plot(X,Y)
    plot.show()

    n = np.sin(X) + np.cos(Y) + np.random.uniform(0, 1, X.shape)
    plot.imshow(n)
    plot.show()

    plot.imshow(np.fft.fftn(n).astype(np.uint8))
    plot.show()
    



