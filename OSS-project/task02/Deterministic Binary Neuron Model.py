import numpy as np

def sgn(s):
    if s >= 0: x = 1
    else: x = 0
    return x

class DHNN:
    def __init__(self, trainData):
        # initialization
        self.n = np.size(s0) # number of neurons
        self.W = np.diag(np.zeros(self.n)) # weights 
        self.S = s0 # states of neurons
        self.train(trainData)

    def train(self, sample):
        # Learning weights 
        for i in range(self.n):
            for j in range(self.n):
                delta = 1 if i == j else 0
                a = []
                for m in sample:
                    a_ = m[i] * m[j]
                    a.append(a_)
                self.W[i,j] = (1-delta) * np.sum(a)
        return self.W

    def energy(self, currState = []):
        state = currState
        #E = (-0.5) * np.dot(np.dot(state.T, self.W), state)
        E = np.dot(np.dot(state.T, self.W), state)
        return E

    #def update(self, currStates):
    def update(self, S):
        #tempStates = currStates
        tempStates = S

        #Compute the initial energy
        E = self.energy(tempStates)
        #print(E)

        # Update a neuron randomly 
        idx = np.random.randint(0, self.n)
        enerChange = np.dot(self.W[idx].T, tempStates)
        tempStates[idx] = sgn(enerChange)

        #Compute the updated energy
        Enew = self.energy(tempStates)
        #print(Enew)
        if Enew >= E:
            return S
        else:
            E = Enew
            return tempStates

if __name__ == '__main__':
    St = np.array([[1, -1, 1, 1], [-1, 2, -1, -1], [2, -1, 2, 1], [-1, -1, 1, 1]])
    s0 = np.array([1, 1, 1, 1])
    energy = []
    sCurr = s0
    test = DHNN(s0, St)


    for i in range(30):
        sCurr = test.update(sCurr)
        #energy.append(test.energy(sCurr))
        while test.energy(sCurr) == 0:
            break
    
    print(energy)
    print(sCurr)


"""
    while test.energy(sCurr) > 0:
        sCurr = test.update(sCurr)
        print(sCurr)
        energy.append(test.energy(sCurr))
"""
