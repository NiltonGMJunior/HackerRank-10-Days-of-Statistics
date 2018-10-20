def mean(x, n):
    return sum(x)/n

def median(x):
    x.sort()
    while True:
        if len(x) <= 2:
            return mean(x, len(x))
        else:
            x = x[1:-1]

def getQuartils(x, n):
    x.sort()
    if n % 2 == 0:
        l = x[:n//2]
        u = x[n//2:]
        q2 = median([l[-1], u[0]])
    else:
        l = x[:n//2]
        u = x[n//2 + 1:]
        q2 = x[n//2]

    q1 = median(l)
    q3 = median(u)

    return tuple(map(int, (q1, q2, q3)))

if __name__ == "__main__":

    # n = int(input())
    # x = list(map(int, input().split(" ")))

    n = int('10')
    x = list(map(int, "3 7 8 5 12 14 21 15 18 14".split(" ")))

    print(getQuartils(x, n)[0])
    print(getQuartils(x, n)[1])
    print(getQuartils(x, n)[2])
