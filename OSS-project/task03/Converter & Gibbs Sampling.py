# Here is the source code of task 3: Make a converter to compute the weight matrix of the given states of neurons from the energy function. Use Gibbs sampling to update the RNN and check if N(x_1, x_2, x_3) follows Boltzmann distribution.
import numpy as np

class HopNet(object):
    def train_weights(self, trainData):
        print("Start to train weights...")
        self.numNeuron = trainData[0].shape[0]

        # Initialize weights
        W = np.diag(np.zeros(self.numNeuron))

        # Hebb rule
        for i in range(self.numNeuron):
            for j in range(self.numNeuron):
                delta = 1 if i == j else 0
                a = []
                for m in trainData:
                    a_ = m[i] * m[j]
                    a.append(a_)
                W[i,j] = (1-delta) * np.sum(a)
        self.W = W
        return self.W

    def energy(self, state):
        return (-0.5)*np.dot(np.dot(state.T, self.W), state) + np.sum(state * self.threshold)

    def update(self, num_iter, initState, threshold = []):
        self.threshold = threshold

        s = initState
        e = self.energy(s)

        for i in range(num_iter):
            idx = np.random.randint(0, self.numNeuron)
            print(idx)
            #s[idx] = np.sign(np.dot(self.W[idx].T, s) - self.threshold)
            s[idx] = np.sign(np.dot(self.W[idx].T, s))
            #print(s)

            e_new = self.energy(s)

            if e == e_new:
                return s
            e = e_new
        return s    

if __name__ == '__main__':
    St = np.array([[1, -2, 1], [-1, 1, 1], [2, -1, -1]]) # Solution: [0, 1, 1]
    s0 = np.array([0, 0, 0])
    threshold = [-1, 2, -2]

    test = HopNet()
    weight = test.train_weights(St)
    
    solution = test.update(30, s0, threshold)



