import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

def cv2Introduction(image):
    print(cv2.__version__)
    imgpath = image #'D:/Dataset/4.2.03.tiff'
    #imgpath = '/home/pi/Dataset/4.2.03.tiff'
    img = cv2.imread(imgpath)

    type(img)

    cv2.imshow('Mandrill', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.namedWindow('Mandrill', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('Mandrill',img)
    cv2.waitKey(0)
    cv2.destroyWindows('Mandrill')

    outpath = 'D:/Dataset/output.jpg'
    cv2.imwrite(outpath, img)

    img = cv2.imread(imgpath,0)
    cv2.imshow('Mandrill',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


    img1 = np.zeros((512,512,3), np.uint8)
    cv2.line(img1, (0, 99), (99, 0), (255, 0, 0), 2)
    cv2.rectangle(img1, (100, 60), (200, 170), (0, 255, 0), 2)
    cv2.circle(img1, (60, 60), 50, (0, 0, 255), -1)
    cv2.ellipse(img1, (100, 200), (50, 20), 0, 0, 360, (127, 127, 127), -1)
    points = np.array([[80, 2], [125, 0], [170, 0], [230, 5], [30, 50]], np.int32)
    points = points.reshape((-1, 1, 2))
    cv2.polylines(img1, [points], True, (0, 255, 255))
    text1 = 'Test Text'
    cv2.putText(img1, text1, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 0))
    cv2.imshow('Shapes', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def emptyFunction():
    pass

def cv2MatGui():

    img1 = np.zeros((512, 512, 3), np.uint8)
    windowName = 'OpenCV Application'
    cv2.namedWindow(windowName)

    cv2.createTrackbar('B', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('G', windowName, 0, 255, emptyFunction)
    cv2.createTrackbar('R', windowName, 0, 255, emptyFunction)

    while True:
        cv2.imshow(windowName, img1)
        
        if cv2.waitKey(1) == 27:
            break
        
        blue = cv2.getTrackbarPos('B', windowName)
        green = cv2.getTrackbarPos('G', windowName)
        red = cv2.getTrackbarPos('R', windowName)
        
        img1[:] = [blue, green, red]
    cv2.destroyAllWindows()

    imgpath = image
    img = cv2.imread(imgpath, 0)

    plt.imshow(img)
    plt.title('Greyscale image with Default Colormap')
    plt.show()

    plt.imshow(img, cmap='gray')
    plt.title('Greyscale image with gray Colormap')
    plt.show()

    img = cv2.imread(imgpath)
    plt.imshow(img)
    plt.title('Color Image BGR')
    plt.show()

    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    plt.imshow(img1)
    plt.title('Color Image RGB')
    plt.show()

    j = 0
    for filename in dir(cv2):
        if filename.startswith('COLOR_'):
            print(filename)
            j = j + 1

    print('There are ' + str((j+1)) + 
        ' color conversion flags in OpenCV ' 
        + cv2.__version__ + ' .')
    
def cv2Processing(dir, image1, image2):
    path = dir
    imgpath1 = path + image1
    imgpath2 = path + image2

    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    mult = img1 * img2
    div = img1 / img2

    titles = ['Liquid Drop', 'Mandrill', 'Multiplication', 'Division']
    images = [img1, img2, mult, div]
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

    alpha = 0.5
    beta = 0.5
    gamma = 0
    # img1 * alpha + img2 * beta + gamma
    output = cv2.addWeighted(img1, alpha, img2, beta, gamma)
    titles = ['Liquid Drop', 'Mandrill', 'Weighted Addition']
    images = [img1, img2, output]
    for i in range(3):
        plt.subplot(1, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.show()


    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    for i in np.linspace(0, 1, 1000):
        alpha = i
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        cv2.imshow('Transition', output)
        time.sleep(0.0001)
        if cv2.waitKey(1) == 27:
            break
    cv2.destroyAllWindows()


    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
    windowName = 'Transition Demo'
    cv2.namedWindow(windowName)
    cv2.createTrackbar('Alpha', windowName, 0, 1000, emptyFunction)
    while True:
        cv2.imshow(windowName, output)
        if cv2.waitKey(1) == 27:
            break
        alpha = cv2.getTrackbarPos('Alpha', windowName) / 1000
        beta = 1 - alpha
        output = cv2.addWeighted(img1, alpha, img2, beta, 0)
        print(alpha, beta)
    cv2.destroyAllWindows()

    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    r, g, b = cv2.split(img1)
    titles = ['Original', 'Red', 'Green', 'Blue']
    images = [cv2.merge((r, g, b)), r, g, b]
    plt.subplot(2, 2, 1)
    plt.imshow(images[0])
    plt.title(titles[0])
    plt.axis('off')
    plt.subplot(2, 2, 2)
    plt.imshow(images[1], cmap='Reds')
    plt.title(titles[1])
    plt.axis('off')
    plt.subplot(2, 2, 3)
    plt.imshow(images[2], cmap='Greens')
    plt.title(titles[2])
    plt.axis('off')
    plt.subplot(2, 2, 4)
    plt.imshow(images[3], cmap='Blues')
    plt.title(titles[3])
    plt.axis('off')
    plt.show()


    img1 = cv2.imread(imgpath1, 1)
    img2 = cv2.imread(imgpath2, 1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img3 = cv2.bitwise_not(img1)
    img4 = cv2.bitwise_and(img1, img2)
    img5 = cv2.bitwise_or(img1, img2)
    img6 = cv2.bitwise_xor(img1, img2)
    titles = ['Image 1', 'Image 2', 'Image NOT', 'AND', 'OR', 'XOR']
    images = [img1, img2, img3, img4, img5, img6]
    for i in range(6):
        plt.subplot(2, 3, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.show()

    x = np.uint8([240])
    y = np.uint8([20])
    print(x + y) # (x + y) % 256
    print(cv2.add(x, y))
    add1 = img1 + img2
    add2 = cv2.add(img1, img2)
    titles = ['Liquid Drop', 'Mandrill', 'NumPy addition', 'cv2.add()']
    images = [img1, img2, img3, img4]
    for i in range(4):
        plt.subplot(1, 4, i+1)
        plt.imshow(images[i])
        plt.title(titles[i])
        plt.axis('off')
    plt.show()


if __name__ == '__main__':
    #cv2Introduction("cintaku.jpg")
    #cv2MatGui()
    cv2Processing(directory, image1, image2)
