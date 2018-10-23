import math

def binomial(x, n, p):
    return math.factorial(n) / math.factorial(x) / math.factorial(n - x) * (p ** x) * ((1 - p) ** (n - x))

if __name__ == '__main__':

    # inp = list(map(int, input().split(" ")))
    inp = list(map(int, "12 10".split(" ")))

    p = inp[0]/100
    n = inp[1]

    result_1 = sum([binomial(x, n, p) for x in range(3)])
    result_2 = sum([binomial(x, n, p) for x in range(2, n + 1)])

    print(round(result_1, 3))
    print(round(result_2, 3))
