import math

def mean(X):
    return sum([elem for elem in X])/len(X)

def std(X):
    return math.sqrt(sum([(elem - mean(X))**2 for elem in X])/len(X))

def cov(X, Y):
    return sum([(elem_X - mean(X))*(elem_Y - mean(Y)) for elem_X, elem_Y in zip(X, Y)])/len(X)

def pearson(X, Y):
    return cov(X, Y) / std(X) / std(Y)

if __name__ == '__main__':

    n = 5

    pairs = []

    for i in range(n):
        pairs.append(tuple(map(int, input().split())))

    X = [elem_x for elem_x, elem_y in pairs]
    Y = [elem_y for elem_x, elem_y in pairs]

    b = pearson(X, Y) * std(Y) / std(X)

    a = mean(Y) - b * mean(X)

    result = a + b*80

    print(round(result, 3))
