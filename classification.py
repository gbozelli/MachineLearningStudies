from matplotlib import pyplot as plt

class car:
    def __init__(self, power, price, signal):
        self.power = power
        self.price = price
        self.signal = signal
        self.x = [power, price]

def createClass(X,Y,S):
    Set = []
    for i in range(0,len(Y)):
        S.append(False)
        if Y[i]<30:
            S[i]=True
    for i in range(0, len(Y)):
        Set.append(car(X[i],Y[i],S[i]))
    return Set

def hypothesisTest(Set):
    SpecificPower = []
    SpecificPrice = []
    GeneralPower = []
    GeneralPrice = []
    for i in range(0,len(Set)):
        if Set[i].signal == True:
            SpecificPower.append(Set[i].power)
            SpecificPrice.append(Set[i].price)
        else:
            GeneralPower.append(Set[i].power)
            GeneralPrice.append(Set[i].price)
    sorted(SpecificPower)
    sorted(SpecificPrice)
    sorted(GeneralPower)
    sorted(GeneralPower)
    SpecificParamether = [[SpecificPower[0],SpecificPrice[0]],[SpecificPower[-1],SpecificPrice[-1]]]
    GeneralParamether = [[GeneralPower[0],GeneralPrice[0]],[GeneralPower[-1],GeneralPrice[-1]]]
    return SpecificParamether, GeneralParamether

def classifier(Set, Paramethers):
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(X,Y,'or')
    plt.show()

def plotGraph():
    fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
    ax.plot(X,Y,'or')
    plt.show()

X = [88,71,18,75,30,52,79,47,44,37,11,23,87,16,93]
Y = [86,30,16,53,22,45,50,90,64,28,68,85,62,11,55]
S = []
Set = createClass(X,Y,S)
SpecificParamether, GeneralParamether = hypothesisTest(Set)
classifier(Set, Paramethers)

