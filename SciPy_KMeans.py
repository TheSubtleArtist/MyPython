import matplotlib_inline as main
import numpy as np
import matplotlib.pyplot as plot
from scipy.cluster.vq import kmeans

data = np.random.rand(100,2)

if __name__ == '__main__':
    centroid, _ = kmeans(data,10)
    plot.scatter(data[:,0],data[:,1])
    plot.scatter(centroid[:,0], centroid[:,1], c='r')
    plot.show()

    