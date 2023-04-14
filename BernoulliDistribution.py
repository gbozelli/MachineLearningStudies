import numpy as np

def f(p,x):
    return (p**x)*(1-p)**(1-x)

def E(p):
    return p

def Var(p):
    return p*(1-p)

def generateSample(p,Size):
    X = []
    while Size>0:
        if np.random.rand() <= p:
            X.append(0)
        else:
            X.append(1)
        Size -= 1
    return X

def generateDistribution(X):
    p = 0
    N = len(X)
    for i in range(0,N):
        p += X[i]
    p /= N
    return p 


