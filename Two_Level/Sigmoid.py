import numpy as np
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def tanh(x):
    return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))