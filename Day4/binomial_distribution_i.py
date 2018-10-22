import math

def binomial(x, n, p):
    return math.factorial(n) / math.factorial(x) / math.factorial(n - x) * (p ** x) * ((1 - p) ** (n - x))

if __name__ == '__main__':
    boys_to_girls = 1.09
    p_boy = boys_to_girls / (boys_to_girls + 1)
    p_girl = 1 - p_boy
    result = sum([binomial(i, 6, p_boy) for i in range(3,7)])
    print(round(result,3))
