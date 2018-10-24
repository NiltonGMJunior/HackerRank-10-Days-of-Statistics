import math

def normal(x, mu, sigma):
    return 0.5 * (1 + math.erf((x - mu) / (sigma * (2 ** 0.5))))

if __name__ == '__main__':

    max_tickets = float(input())

    num_students = int(input())

    mu = float(input())

    sigma = float(input())

    # max_tickets = 250
    #
    # num_students = 100
    #
    # mu = 2.4
    #
    # sigma = 2.0

    result = normal(max_tickets, mu*num_students, sigma*math.sqrt(num_students))

    print(round(result, 4))
