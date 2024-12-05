# https://github.com/ec-council-learning/Applied-Python-for-Professionals/tree/main

import matplotlib_inline
import numpy as np
import matplotlib.pyplot as plot
import scipy.datasets
import scipy.signal
from scipy import ndimage as ndi
from scipy.ndimage import gaussian_filter
from scipy.ndimage import gaussian_gradient_magnitude
from scipy.ndimage import gaussian_laplace
from scipy.ndimage import laplace
from scipy.ndimage import maximum_filter
from scipy.ndimage import median_filter
from scipy.ndimage import minimum_filter
from scipy.ndimage import percentile_filter
from scipy.ndimage import prewitt
from scipy.ndimage import rank_filter
from scipy.ndimage import sobel
from scipy.ndimage import uniform_filter

def imgBasic(image):
    img1 = plot.imread(image)
    plot.imshow(img1)
    plot.axis('off')
    plot.title('Tree')
    plot.show()
    plot.imsave('output.png', img1)
    type(img1)
    img1.shape
    img1.ndim
    img1.size 
    img1.dtype
    img1.nbytes
    img1[10,10,0]
    img1[10,10]
    img1[10,10,:]

def imgStats(image):
    img1 = plot.imread(image)
    # Image Statistics
    img1.min()
    img1.max()
    img1.mean()
    np.median(img1)
    np.average(img1)
    np.mean(img1)
    np.std(img1)
    np.var(img1)

def imgMask(image):
    img1 = plot.imread(image)
    # Image Mask
    nrows,ncols,channels=img1.shape
    row,col = np.ogrid[:nrows,:ncols]
    cnt_row,cnt_col=nrows/2,ncols/2
    outer_disk_mask=((row-cnt_row) ** 2 + (col-cnt_col) ** 2 > (nrows/2) ** 2)
    img1a = img1.copy()
    img1a[outer_disk_mask]=255

    plot.imshow(img1a)
    plot.axis('off')
    plot.title('Masked Image')
    plot.show()

def imgChannels(image):
    img1 = plot.imread(image)
    # Image Channels
    r = img1[:,:,1]
    b = img1[:,:,2]
    g = img1[:,:,3]

    output = [img1,r,g,b]
    titles = ['Image', 'Red', 'Green', 'Blue']
    for i in range(len(titles)):
        plot.subplot(2,2,i+1)
        plot.axis('off')
        plot.title(titles[i])
        if i == 0:
            plot.imshow(output[i])
        else:
            plot.imshow(output[i], cmap='gray')
    plot.show()
    output = np.dstack((r,g,b))
    plot.imshow(output)
    plot.show()

def imgArithmatic(image1, image2):
    img1 = plot.imread(image1)
    img2 = plot.imread(image2)
    # Arithmetic operaitons on Images with Numpy
    plot.imshow(img1)
    plot.show()
    plot.imshow(img1)
    plot.show()

    plot.imshow(img1 + img2)
    plot.show()

    plot.imshow(img2 + img1)
    plot.show()
    
    plot.imshow(img2 - img1)
    plot.show()

    plot.imshow(img1 - img2)
    plot.show()

    plot.imshow(np.flip(img1,-1))
    plot.show()

    plot.imshow(np.flip(img1,-2))
    plot.show()

    plot.imshow(np.flip(img1,0))
    plot.show()

    plot.imshow(np.flip(img1,1))
    plot.show()

    plot.imshow(np.flip(img1,2))
    plot.show()

    plot.imshow(np.roll(img2,2048))
    plot.show()

    plot.imshow(np.flip1r(img1))
    plot.show()

    plot.imshow(np.flipud(img1))
    plot.show()

    plot.imshow(np.rot90(img1))
    plot.show()

def imgLogical(image1, image2):
    img1 = plot.imread(image1)
    img2 = plot.imread(image2)
    # Logical Operations
    plot.imshow(np.bitwise_and(img1, img2))
    plot.show()
    plot.imshow(np.bitwise_or(img1,img2))
    plot.show()
    plot.imshow(np.bitwise_and(img2,img1))
    plot.show()

    plot.subplot(1,2,1)
    plot.imshow(np.bitwise_xor(img1,img2))
    plot.subplot(1,2,2)
    plot.imshow(np.bitwise_xor(img2,img1))
    plot.show()

    plot.subplot(1,2,1)
    plot.imshow(img1)
    plot.subplot(1,2,2)
    plot.imshow(np.bitwise_not(img1))
    plot.show()

def imgHistograms(image):
    img1 = plot.imread(image)
    r = img1[:,:,1]
    b = img1[:,:,2]
    g = img1[:,:,3]

    plot.subplots_adjust(hspace=0.5, wspace=0.5)

    plot.subplot(2,2,1)
    plot.title('Original Image')
    plot.imshow(img1)

    hist,bins = np.histogram(r.ravel(), bins=256,range=(0,256))
    plot.subplot(2,2,2)
    plot.title('Red Historgram')
    plot.bar(bins[:-1], hist)

    hist,bins = np.histogram(g.ravel(), bins=256,range=(0,256))
    plot.subplot(2,2,3)
    plot.title('Green Historgram')
    plot.bar(bins[:-1], hist)

    hist,bins = np.histogram(b.ravel(), bins=256,range=(0,256))
    plot.subplot(2,2,4)
    plot.title('Green Historgram')
    plot.bar(bins[:-1], hist)

    plot.show()

    plot.subplots_adjust(hspace=0.5, wspace=0.5)

    plot.subplot(2, 2, 1)
    plot.title('Original Image')
    plot.imshow(img1)

    plot.subplot(2, 2, 2)
    plot.title('Red Histogram')
    plot.hist(r.ravel(), bins=256, range=(0, 256))

    plot.subplot(2, 2, 3)
    plot.title('Green Histogram')
    plot.hist(g.ravel(), bins=256, range=(0, 256))

    plot.subplot(2, 2, 4)
    plot.title('Blue Histogram')
    plot.hist(b.ravel(), bins=256, range=(0, 256))

def imgMiscMeasures(image):
    ascent = scipy.datasets.ascent()
    face = scipy.datasets.face()
    ecg = scipy.datasets.electrocardiogram()

    plot.imshow(ascent, cmap='gray')
    plot.show()

    plot.imshow(face)
    plot.show()

    plot.plot(np.arange(108000), ecg)
    plot.show()

def imgMultiDim(image):
    ascent = scipy.datasets.ascent()
    ndimage.center_of_mass(ascent)
    ndimage.extrema(image)
    ndimage.find_objects(ascent)
    ndimage.maximum(ascent)
    ndimage.mean(ascent)
    ndimage.median(ascent)
    ndimage.minimum(ascent)
    ndimage.standard_deviation(ascent)
    ndimage.sum(ascent)
    ndimage.variance(ascent)

def imgConvolution(image):
    ascent = scipy.datasets.ascent()
    kernel = np.array([[0,-1,0],[-1,23,-1],[0,-1,0]], dtype=np.int8)
    image_sharpen = scipy.signal.convolve2d(ascent,kernel)
    plot.imshow(image_sharpen, cmap='gray')
    plot.show()

    kernel = np.array([[-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -6, -1, -1],
                  [-1, -1, -1, -1, -1],
                  [-1, -1, -1, -1, -1]], dtype=np.int8)
    
    edges = scipy.signal.convolve2d(ascent, kernel)
    plot.imshow(edges, cmap='gray')
    plot.show()

    kernel = np.ones((15, 15))/255
    print(kernel)
    blur = scipy.signal.convolve2d(ascent, kernel)
    plot.imshow(blur, cmap='gray')
    plot.show()

    kernel = np.ones((7, 7))/49
    print(kernel)
    blur = scipy.signal.convolve2d(ascent, kernel)
    plot.imshow(blur, cmap='gray')
    plot.show()

def imgFilters(image):
    ascent = scipy.datasets.ascent()
    face = scipy.datasets.face()
    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(gaussian_filter(ascent, sigma=3) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(gaussian_filter(ascent, sigma=15) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(gaussian_gradient_magnitude(ascent, sigma=3) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(gaussian_gradient_magnitude(ascent, sigma=9) , cmap='gray')
    plot.show()


    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(gaussian_laplace(ascent, sigma=1) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(laplace(ascent) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(maximum_filter(ascent, size=15) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(median_filter(ascent, size=17) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(minimum_filter(ascent, size=17) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(percentile_filter(ascent, percentile=20, size=20) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(prewitt(ascent) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(rank_filter(ascent, rank=42, size=20) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(sobel(ascent) , cmap='gray')
    plot.show()

    plot.subplot(1, 2, 1)
    plot.imshow(ascent, cmap='gray')
    plot.subplot(1, 2, 2)
    plot.imshow(uniform_filter(ascent, size=20) , cmap='gray')
    plot.show()

def imgMorphology(image):
    
    img = np.zeros((32,32))
    img[8:-8,8,-8]
    plot.imshow(image)
    plot.show()

    dist1 = ndi.distance_transform_bf(img)
    plot.imshow(dist1)
    plot.title('Brute Force')
    plot.show()

    dist1=ndi.distance_transform_cdt(img)
    plot.imshow(dist1)
    plot.title('Chamfer')
    plot.show()

    dist1 = ndi.distance_transform_edt(img)
    plot.imshow(dist1)
    plot.title('Euclidian')
    plot.show()

    img = np.zeros((16,16))
    img[4:-4,4:-4]
    print(img)
    plot.imshow(img)
    plot.show()

    erosion=ndi.binary_erosion(img).astype(img.dtype)
    plot.imshow(erosion)
    plot.show()

    dialation=ndi.binary_dialation(img).astype(img.dtype)
    plot.imshow(dialation)
    plot.show()

    opening = ndi.binary_opening(img).astype(img.dtype)
    plot.imshow(opening)
    plot.show()

    closing = ndi.binary_closing(img).astype(img.dtype)
    plot.imshow(closing)
    plot.show()

    img = np.ones((32,32))

    x,y = (32 * np.random.random((2,20)).astype(np.int8))
    img[x,y]
    plot.imshow(img)
    plot.show()

    noise_removed = ndi.binary_fill_holes(img).astype(np.int8)
    plot.imshow(noise_removed)
    plot.show()

    img = np.zeros((16, 16))
    img[4:-4, 4:-4] = 1
    print(img)

    dilation = ndi.grey_dilation(img, size=(3, 3))
    plot.imshow(dilation)
    plot.show()

    erosion = ndi.grey_erosion(img, size=(3, 3))
    plot.imshow(erosion)
    plot.show()

    opening = ndi.grey_opening(img, size=(3, 3))
    plot.imshow(opening)
    plot.show()

    closing = ndi.grey_closing(img, size=(3, 3))
    plot.imshow(closing)
    plot.show()


if __name__ == '__main__':
    imgBasic('resources/output.png')
    imgStats('resources/output.png')
    imgMask('resources/output.png')
    imgChannels('resources/output.png')
    imgHistograms('resources/output.png')
    imgArithmatic('resources/output.png','cintaku.jpg')
    imgLogical('resources/output.png','cintaku.jpg')
    imgMiscMeasures('image')
    imgMultiDim(image)
    imgConvolution(image)
    imgFilters(image)
    imgMorphology(image)

