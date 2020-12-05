import numpy as np
from numpy.random import *
from math import *


class SA:
    def __init__(self, initT, initS, numIter, alpha, trainData, theta):
        self.s = initS
        self.n = np.size(initS)
        self.W = np.diag(np.zeros(self.n))
        self.T = initT
        self.iter = numIter
        self.alpha = alpha
        self.theta = theta
        self.train(trainData)
    
    def train(self, sample):
        for i in range(self.n):
            for j in range(self.n):
                delta = 1 if i == j else 0
                a = []
                #print(sample)
                for m in sample:
                    a_ = m[i] * m[j]
                    a.append(a_)
                self.W[i,j] = (1-delta) * np.sum(a)
        return (-2)*self.W

    def energy(self, state):
        E = -(0.5) * np.dot(np.dot(self.s.T, self.W), state) + np.dot(self.theta.T, state)
        return E
    
    def prob(self, deltaE):
        p = 1 / (1+np.exp(-abs(deltaE) / self.T))
        return p

    def update(self):
        print("The current temperature is", self.T) 

        currSt = self.s
        currEnergy = self.energy(currSt)
        randNum = np.random.random()

        idx = np.random.randint(0, self.n)
        tempSt = self.s
        # Generate a new state
        tempSt[idx] = 1 - self.s[idx]
    
        tempEnergy = self.energy(tempSt)

        deltaE = tempEnergy - currEnergy
        p = self.prob(deltaE)

        self.T *= self.alpha    

        if deltaE < 0:
            return tempSt
        else:
            if randNum < p:
                if currSt[idx] == 0:
                    tempSt[idx] = 1
                    return tempSt
            else: 
                tempSt[idx] = 0
                return tempSt
        return currSt


if __name__ == "__main__":
    St = np.array([[1, -2, 1], [-1, 1, 1], [2, -1, -1]])
    initS = np.array([1, 1, 1])
    threshold = np.array([20, -6, -3])
    s0 = np.array([0, 0, 0])
    s1 = np.array([1, 0, 0])
    s2 = np.array([0, 1, 0])
    s3 = np.array([0, 0, 1])
    s4 = np.array([1, 1, 0])
    s5 = np.array([0, 1, 1])
    s6 = np.array([1, 0, 1])
    s7 = np.array([1, 1, 1])
    counter = [0]*8

    test = SA(initT=10, initS = initS, numIter=1000, alpha=0.99, trainData = St, theta=threshold)
    
    for i in range(1000):
        currS = test.update()
        print("The current state is", currS)
        if (currS == s0).all(): 
            counter[0] += 1
        if (currS == s1).all():
            counter[1] += 1
            #print("The current state is", currS)
        elif (currS == s2).all():
            counter[2] += 1
        elif (currS == s3).all():
            counter[3] += 1
        elif (currS == s4).all():
            counter[4] += 1
        elif (currS == s5).all():
            counter[5] += 1
        elif (currS == s6).all():
            counter[6] += 1
        elif (currS == s7).all():
            counter[7] += 1

    print("The frequency of all states is", counter)
    print("The frequency of state [0, 1, 1] is", counter[5])

  

    
        
