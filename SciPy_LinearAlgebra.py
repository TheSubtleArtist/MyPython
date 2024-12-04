import numpy as np
import scipy.linalg as sca

x=np.array([[0,2,3],[4,5,6],[7,8,9]])
a=np.array([[2,1,-3],[4,-2,1],[3,5,-2]])
b = np.array([-4, 9, 5])
c=np.arange(36).reshape((6,6))
d=np.arange(49).reshape((7,7))

if __name__ == '__main__':
    print("Array(x): \n",x)
    print("Inverse(x): \n", sca.inv(x))
    print("Array(a): \n",a)
    print("Array(b): \n",b)
    print("Solve a(x)=b: \n", sca.solve(a,b))
    print("Solve the determinant: \n", sca.det(a))
    print("Solve the norm: \n", sca.norm(a))
    print("Array(c): \n", c)
    #print("Lower trangle matrix (c):\n", sca.tril(c,k=0))
    #print("Lower trangle matrix (c):\n", sca.tril(c,k=-1))
    #print("Lower trangle matrix (c):\n", sca.tril(c,k=1))
    #print("upper trangle matrix (c):\n", sca.triu(c,k=1)) 
    print("Array(d): \n", d)

    p,l,u = sca.lu(d) #Compute LU decomposition of a matrix with partial pivoting.
    print("p: \n", p)
    print("l: \n",l)
    print("u:\n", u)

    q,r=sca.qr(d) #Compute QR decomposition of a matrix with partial pivoting.
    print("q: ", q)
    print("r: \n", r)


