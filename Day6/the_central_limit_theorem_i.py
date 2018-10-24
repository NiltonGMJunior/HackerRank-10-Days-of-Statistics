import math

def normal(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

if __name__ == '__main__':

    # max_weigth = float(input())
    #
    # num_boxes = int(input())
    #
    # mu = float(input())
    #
    # sigma = float(input())

    max_weigth = 9800

    num_boxes = 49

    mu = 205

    sigma = 15

    result = normal(max_weigth, mu*num_boxes, sigma*math.sqrt(num_boxes))

    print(round(result, 4))
