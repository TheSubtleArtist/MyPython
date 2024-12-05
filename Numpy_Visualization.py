# https://github.com/ec-council-learning/Applied-Python-for-Professionals/tree/main
import numpy as np
from matplotlib import pyplot as plot

def simpleMatPlot(number):
    x = np.arange(number)
    print(x)
    type(x)
    y=x+1
    plot.plot(x,y,'o-')
    plot.show()




if __name__ == '__main__':
    arrOneDim = np.empty(3, np.uint8)
    print("Empty: New array of given shape and type (1D):\n", arrOneDim)

    arrTwoDim = np.empty([3,3], np.uint8)
    print("Empty: New Array of given shaape and type (2D):\n",arrTwoDim)

    arrThreeDim = np.empty([3,3,3], np.uint8)
    print("Empty: Newa array of given shape and type (3D):\n",arrThreeDim)

    matIdFive = np.eye(5, dtype=np.uint8)
    print("Eye: 2D array wiht ones on the diagnoal and zeros fill in:\n", matIdFive)

    matIdFiveOne = np.eye(5, dtype=np.uint8, k=1)
    print("Eye: shift the diagonal up one:\n", matIdFiveOne)

    matIdFiveNegOne = np.eye(5, dtype=np.uint8, k=-1)
    print("Eye: Shift the diagonal down one: :\n", matIdFiveNegOne)

    matIdOneTwoFives = np.ones ((2,5,5),dtype=np.int16)
    print("Ones: 2D array filled with Ones: \n", matIdOneTwoFives)

    matIdZeroTwoFives = np.zeros ((2,5,5),dtype=np.int16)
    print("Zeros: New 2D array filled with zeros: \n", matIdZeroTwoFives)

    matIdCustomFill = np.full((2,5), dtype=np.int16, fill_value=5)
    print("Fill: New 2D array filled with a custom value fill: \n", matIdCustomFill)

    matTriangle = np.tri(3,3,k=0,dtype=np.uint16)
    print("Tri: Array with ones at and below the given diagonal: \n", matTriangle)

    matTriangleUp = np.tri(3,3,k=1,dtype=np.uint16)
    print("Tri: array with ones at and below the given diagonal, shift up from home: \n", matTriangleUp)

    matTriangleDn = np.tri(3,3,k=-1,dtype=np.uint16)
    print("Tri: array with ones at and below the given diagonal, shift down from home: \n", matTriangleDn)

    matTriangleFives = np.ones((5,5),dtype=np.int8)
    print("Upper Triangle Matrix of matTriangleFives:\n", matTriangleFives)
    # Upper and Lower Trianlge Matrices
    print("Tril: copy an array with elements above the k-th diagnoal zeroed:\n",np.tril(matTriangleFives))
    print("Tril k+1:\n",np.tril(matTriangleFives, k=1))
    print("Tril k-1:\n",np.tril(matTriangleFives, k=-1))  
    print("Triu: Copy an array with elements below the k-th diagonal zeroed: \n",np.triu(matTriangleFives))
    print("Triu k+1:\n",np.triu(matTriangleFives, k=1))
    print("Triu k-1:\n",np.triu(matTriangleFives, k=-1))
    # MatPlotLib
    arrBase = np.arange(6)
    print("Evenly spaced values within a given range: \n",arrBase)

    arrBasePlus=arrBase+1
    print("arrBase plus one:\n",arrBasePlus)
    plot.plot(arrBase,arrBasePlus, 'o--')
    plot.show()

    arrBaseRange = np.arange(2,6,.5)
    print("A custom range with float steps:\n",arrBaseRange)
    plot.plot(arrBase,arrBasePlus, 'o--')
    plot.plot(arrBase,-arrBasePlus, 'o-')
    plot.title('y=f(x)=x')
    plot.show()

    # Linspace
    arrLinspace = np.linspace(0,15,15) # generate a line with starting point of zero, ending point of 15 and 16 points.
    print("linspace: \n", arrLinspace)
    arrLinspace2x = arrLinspace * 2
    plot.plot(arrLinspace, arrLinspace2x, 'o-')
    plot.axis('off')
    plot.show()

    #Logspace
    arrLogspace = np.logspace(0.1,2,15) # generate a line with starting point of zero, ending point of 15 and 16 points.
    print('logspace:\n', arrLogspace)
    plot.plot(arrLogspace, arrLinspace2x, 'o-')
    plot.axis('on')
    plot.show()

    # Geometric Space
    arrGeospace = np.geomspace(0.1,2000,15) # generate a line with starting point of zero, ending point of 15 and 16 points.
    print('Gepspace:\n', arrGeospace)
    plot.plot(arrGeospace, arrLinspace2x, 'o-')
    plot.axis('on')
    plot.show()

    simpleMatPlot(int(input("Enter a number: ")))

