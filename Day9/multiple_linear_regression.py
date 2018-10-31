import numpy as np
from numpy.linalg import inv

if __name__ == '__main__':

    m, n = tuple(map(int, input().split()))

    X_train= []
    Y_train = []

    for i in range(n):
        inp = list(map(float, input().split()))
        X_train.append([1] + inp[:-1])
        Y_train.append(inp[-1])

    X_train = np.array(X_train)
    Y_train = np.reshape(np.array(Y_train), (n, 1))

    B = np.matmul(inv(np.matmul(np.transpose(X_train), X_train)), np.matmul(np.transpose(X_train), Y_train))

    t = int(input())

    for i in range(t):
        X_test = [1] + list(map(float, input().split()))
        Y_test = np.matmul(np.array(X_test), B)
        print(round(float(Y_test), 2))
