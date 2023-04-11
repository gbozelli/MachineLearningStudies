import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def graphic(x,X,Y):
    x1 = np.linspace(0, 5, 100)
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(x1, x1*x[1] + x[0], label=('',len(x)-1,'rd order'))
    ax.plot_date(X,Y)
    plt.show()
    return None

def Regression(X,Y,order):
    A = createMatrix(order,order)
    B = []
    for i in range(0,order+1):
        B.append(0)
    A = valuesMatrix(A, X)
    B = valuesVector(B, Y)
    print(A)
    print(B)
    x = np.linalg.solve(A,B)
    return x

def createMatrix(m,n):
    Matrix = []
    Element = []
    for i in range(0,m+1):
        Element = []
        Matrix.append(Element)
        for j in range(0,n+1):
            Element.append(0)
    return Matrix

def valuesMatrix(Matrix,Sample):
    m = len(Matrix)
    n = len(Matrix[0])
    Size = len(Sample)
    for i in range(0,m):
        for j in range(0,n):
            for k in range(0,Size):
                Matrix[i][j] += Sample[k]**(i+j)
    Matrix[0][0] = Size
    return Matrix

def valuesVector(Matrix,Sample):
    m = len(Matrix)
    Size = len(Sample)
    for i in range(0,m):
        for k in range(0,Size):
            Matrix[i] += Sample[k]**(i)
    return Matrix

Y = [11,19,29,31,40.5,50]
X = [1,2,3,3,4,5]
x = Regression(X,Y,1)
print(x)
graphic(x,X,Y)

