import math

def normal(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

if __name__ == '__main__':

    # [mu, sigma] = list(map(float, input().split()))
    #
    # a = float(input())
    #
    # [b1, b2] = list(map(float, input().split()))

    [mu, sigma] = list(map(float, "20 2".split()))

    a = float("19.5")

    [b1, b2] = list(map(float, "20 22".split()))

    result_a = normal(a, mu, sigma)

    result_b = normal(b2, mu, sigma) - normal(b1, mu, sigma)

    print(round(result_a, 3))

    print(round(result_b, 3))
