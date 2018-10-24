import math

def cost(l, a, b, k_lim):
    return sum([poisson(k, l)*(a + b*k**2) for k in range(k_lim)])

def poisson(k, l):
    return (l ** k) * (math.e ** (-l)) / math.factorial(k)

if __name__ == '__main__':

    # l = list(map(float, input().split()))

    l = list(map(float, "0.88 1.55".split()))
    l_A = l[0]
    l_B = l[1]

    #   A average cost
    k_lim = 1
    while True:
        cost_nowA, cost_nextA = round(cost(l_A, 160, 40, k_lim), 3), round(cost(l_A, 160, 40, k_lim + 1), 3)
        if cost_nowA == cost_nextA:
            break
        k_lim += 1

    #   B average cost
    k_lim = 1
    while True:
        cost_nowB, cost_nextB = round(cost(l_B, 128, 40, k_lim), 3), round(cost(l_B, 128, 40, k_lim + 1), 3)
        if cost_nowB == cost_nextB:
            break
        k_lim += 1

    print(cost_nowA)
    print(cost_nowB)
