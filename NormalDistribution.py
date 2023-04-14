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
    mean = mean(X)
    for i in range(0,len(X)):
        variance += (X[i] - mean)**2
    variance = np.sqrt(deviationof(X))
    return variance

def selectElements(X,mean,deviation):
    X.append(np.random.randint(0,mean))
    X.append(np.random.randint(mean,mean*2))
    meanTest = meanof(X)
    DeviationTest = deviationof(X)
    if meanTest == mean and DeviationTest == deviation:
        return None 
    else:
        X.remove(X[-1])
        X.remove(X[-2])
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

X = generateSample(4,2,2)
Y = []
Y.append(generateDistribution(X))
print(X)
print(Y)
