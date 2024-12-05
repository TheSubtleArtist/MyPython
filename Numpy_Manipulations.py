# https://github.com/ec-council-learning/Applied-Python-for-Professionals/tree/main

import numpy as np

def showOne2Two():
    a = np.arange(6)
    print("one dimension: \n", a)
    print("Reshape: single dimensional to two dimensional: \n", a.reshape(3,2))

def showTwo2One():
    b = np.array([[0,1,2],[7,8,9]])
    print("Two dimensions: \n", b)
    print("one dimensions: \n", np.reshape(b,6))

def showRavel():

    c = np.array([[0,1,2],[7,8,9]])
    print("two dimensions: \n", c)
    print("Ravel: reshape from any dimension to a linear array: \n", np.ravel(c))

def showFlatten():
    d = np.array([[0,1,2],[7,8,9]])
    print("two dimensions")
    print("Return a copy of the array collapsed into one dimension, C style:\n", d.flatten('C'))
    print("Return a copy of the array collapsed into one dimension, F style:\n", d.flatten('F'))

def showStack():
    e = np.array([1,2,3,4], dtype=np.uint8)
    f = np.array([5,6,7,8], dtype=np.uint8)
    print(e,f)
    print('apply the stack: \n', np.stack((e,f)))
    print('apply the stack axis=1: \n', np.stack((e,f), axis=1))
    print('apply the stack axis=1: \n', np.stack((e,f), axis=1).shape)
    print('apply the stack axis=-1: \n', np.stack((e,f), axis=-1))
    print('apply the stack axis=-1: \n', np.stack((e,f), axis=-1).shape)
    print('apply the depth-wise stack : \n', np.dstack((e,f)))
    print('apply the horizontal stack : \n', np.hstack((e,f)))
    print('apply the vertical stack : \n', np.vstack((e,f)))

def showStackSplit():
    g = np.arange(9)
    h, i, j = np.split(g, 3)
    print('Split into equal divisions:\n ', h,i,j )

    m = np.random.rand(4,4,4)
    print('a 4x4x4: \n', m)
    n, o = np.split(m, 2)
    print("stack split randos: \n", n, o)
    p,q = np.dsplit(m,2)
    print("split by depth:\n", p,q)
    r,s = np.hsplit(m,2)
    print('Horizontal split \n', r,s)
    t,u = np.vsplit(m,2)
    print("Vertical Split: \n", t,u)
    v = np.flip(m, axis = 0)
    print("flip along the 0 vertical axis: \n", v)
    w = np.flip(m, axis = 1)
    print("flip along the 1 horizontal axis: \n", w)
    


if __name__ == '__main__':
    print("Rehsape")
    showOne2Two()
    showTwo2One()
    print("Ravel")
    showRavel()
    print("flatten")
    showFlatten()
    print("Stack")
    showStack()
    print('Stack Split')
    showStackSplit()


