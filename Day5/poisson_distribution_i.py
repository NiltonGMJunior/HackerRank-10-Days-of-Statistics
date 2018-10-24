import math

def poisson(k, l):
    return (l ** k) * (math.e ** (-l)) / math.factorial(k)

if __name__ == '__main__':

    l = float(input())
    k = float(input())

    print(round(poisson(k, l), 3))
