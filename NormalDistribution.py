import numpy as np

def test(x,y):
    if x==y:
        return True
    else:
        return False

def summation(X):
    sum = 0
    for i in range(0,len(X)):
        sum += X[i]
    return sum

def summationSquared(X):
    sum = 0
    for i in range(0,len(X)):
        sum += X[i]**2
    return sum

def meanof(X):
    mean = summation(X)/len(X)
    return mean

def deviationof(X):
    deviation = 0
    mean = meanof(X)
    for i in range(0,len(X)):
        deviation += (X[i] - mean)**2
    deviation = np.sqrt(deviation)
    return deviation

def varianceof(X):
    variance = 0
    mean = meanof(X)
    for i in range(0,len(X)):
        variance += (X[i] - mean)**2
    variance = np.sqrt(deviationof(X))
    return variance

def test(X,u,d):
    meanTest = meanof(X)
    DeviationTest = deviationof(X)
    if meanTest == u and DeviationTest == d:
        return None 
    else:
        X.remove(X[-1])
        X.remove(X[-2])
    return None

def avaliateNum(X,mean,deviation):
    u, d = mean, deviation
    k = len(X)
    SumX = summation(X)
    SumX2 = summationSquared(X)
    x = ((u*d**2)-(SumX2)+2*u*(SumX)-u**2)/((k*u)-SumX)-1
    return x

def selectElements(X,mean,deviation):
    u, d = mean, deviation
    k = len(X)
    X.append(np.random.randint(0,mean))
    if(k*u!=summation(X)):
        X.append(avaliateNum(X,mean,deviation))
        test(X,u,d)
    else:
        selectElements(X,u,d)
    return None

def generateSample(mean, deviation, N):
    X = []
    X.append(mean*3/2)
    while len(X) < N:
       selectElements(X,mean,deviation)
    return X

def generateDistribution(X):
    mean = meanof(X)
    deviation = deviationof(X)
    return [mean,deviation]

X = generateSample(4,2,6)
Y = []
Y.append(generateDistribution(X))
print(X)
print(Y)
