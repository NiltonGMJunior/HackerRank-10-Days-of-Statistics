import math

def normal(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

if __name__ == '__main__':

    # [mu, sigma] = list(map(float, input().split()))
    #
    # a = float(input())
    #
    # b = float(input())

    [mu, sigma] = list(map(float, '70 10'.split()))

    a = float("80")

    b = float("60")

    result_1 = (1 - normal(a, mu, sigma))*100

    result_2 = (1 - normal(b, mu, sigma))*100

    result_3 = normal(b, mu, sigma) * 100

    print(round(result_1, 2))

    print(round(result_2, 2))

    print(round(result_3, 2))
