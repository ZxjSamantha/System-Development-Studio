import numpy as np
from random import choice 

def sigmoid(z):
    return 1 / (1+np.exp(-z))

def energyFunc(states = []):
    length = len(states)
    x = list(range(length))
    for i in range(length):
        x[i] = states[i]
    E = (x[0] - x[1] + x[2] + x[3] -2)**2 + ((-1)*x[0] + 2*x[1] -x[2] -x[3] + 2)**2 + (2*x[0] - x[1] + 2*x[2] + x[3] -4)**2 + ((-1)*x[0] + (-1)*x[1] + x[2] + x[3])**2 
    return E

def statesUpdate(currentStates = []):
    tempStates = currentStates
    neuron = choice(currentStates)
    idx = currentStates.index(neuron)
    tempStates[idx] = 1 - currentStates[idx]
    energyChange = energyFunc(tempStates) - energyFunc(currentStates)
    if energyChange < 0: 
        return tempStates
    else: return currentStates

if __name__ == "__main__":
    initialStates = [0, 0, 0, 0]
    #initialStates = [1, 1, 1, 1]
    #initialStates = [0,1,0,1]
    currentStates = initialStates
    energy = []
    while(energyFunc(currentStates) > 0):
        currentStates = statesUpdate(currentStates)
        print(currentStates)
        energy.append(energyFunc(currentStates))
    print(energy)
