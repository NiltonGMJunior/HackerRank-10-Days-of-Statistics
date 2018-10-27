import math

def mean(X):
    return sum([elem for elem in X])/len(X)

def std(X):
    return math.sqrt(sum([(elem - mean(X))**2 for elem in X])/len(X))

def cov(X, Y):
    return sum([(elem_X - mean(X))*(elem_Y - mean(Y)) for elem_X, elem_Y in zip(X, Y)])/len(X)

if __name__ == '__main__':

    # n = int(input())
    # X = list(map(float, input().split()))
    # Y = list(map(float, input().split()))

    n = int('10')
    X = list(map(float, "10 9.8 8 7.8 7.7 1.7 6 5 1.4 2".split()))
    Y = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))

    mean_X = mean(X)
    mean_Y = mean(Y)
    std_X = std(X)
    std_Y = std(Y)
    cov_XY = cov(X, Y)

    pearson = cov_XY / std_X / std_Y

    print(round(pearson, 3))
