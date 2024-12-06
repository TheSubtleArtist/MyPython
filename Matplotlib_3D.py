import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter


def parametricCurve():
    mpl.rcParams['legend.fontsize'] = 10
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')
    theta = np.linspace ( -4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z, label='parametric curve')
    ax.legend()
    plt.show()

def wireframeNotDense():
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.1)
    ax.plot_wireframe(X, Y, Z,
                    rstride=10,
                    cstride=10)
    plt.show()

def simpleSurfacePlot():
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')
    X, Y, Z = axes3d.get_test_data(0.1)
    ax.plot_surface(X, Y, Z,
                    rstride=10,
                    cstride=10)
    plt.show()

def complexSurfacePlot():
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')

    # own Data
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    # polar coordinates
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def simpleContour():
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')

    X, Y, Z = axes3d.get_test_data(0.05)

    cset = ax.contour(X, Y, Z, cmap=cm.coolwarm)
    ax.clabel(cset, fontsize=9, inline=1)

    plt.show()

def complexContour():
    # draw a surface and show the surface contours
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')

    X, Y, Z = axes3d.get_test_data(0.05)

    ax.plot_surface(X, Y, Z,
                    rstride=8,
                    cstride=8,
                    alpha=0.3)

    cset = ax.contour(X, Y, Z, zdir='z',
                    cmap=cm.coolwarm,
                    offset=-100)
    cset = ax.contour(X, Y, Z, zdir='x',
                    cmap=cm.coolwarm,
                    offset=-40)
    cset = ax.contour(X, Y, Z, zdir='y',
                    cmap=cm.coolwarm,
                    offset=40)


    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    ax.set_xlim(-40, 40)
    ax.set_ylim(-40, 40)
    ax.set_zlim(-100, 100)

    plt.show()

def contourThreeD():
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')

    X, Y, Z = axes3d.get_test_data(0.05)

    cset = ax.contour(X, Y, Z, cmap=cm.coolwarm, extend3d=True)

    ax.clabel(cset, fontsize=9, inline=1)

    plt.show()

def bargraphThreeD():
    fig = plt.figure()
    ax =fig.add_subplot(111, projection='3d')

    for c, z in zip(['r', 'g', 'b', 'k'],
                [30, 20, 10, 0]):
        xs = np.arange(20)
        ys = np.random.rand(20)
        
        cs = [c] * len(xs)
        ax.bar(xs, ys, zs=z, zdir='y',
            color=cs, alpha=0.8)

    plt.show()

def streamplotThreeD():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    x, y, z = np.meshgrid(np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.2),
                        np.arange(-0.8, 1, 0.8))

    u = np.sin(np.pi * x ) * np.cos(np.pi * y ) * np.cos(np.pi * z)
    v = -np.sin(np.pi * x ) * np.sin(np.pi * y ) * np.cos(np.pi * z)
    w = (np.sqrt(2.0 / 3.0)*np.cos(np.pi*x) * np.cos(np.pi * y ) * np.sin(np.pi * z))

    ax.quiver(x, y , z, u, v, w, length=0.1, normalize=True)

    plt.show()

       
    


if __name__ == '__main__':
    parametricCurve()
    wireframeNotDense()
    simpleSurfacePlot()
    complexSurfacePlot()
    simpleContour()
    complexContour()
    contourThreeD()
    bargraphThreeD()
    streamplotThreeD()
