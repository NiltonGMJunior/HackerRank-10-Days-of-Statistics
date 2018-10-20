def createFreqSet(x, f, n):

    rtn = []

    for index, x_i in enumerate(x):
        rtn += [x_i]*f[index]

    return rtn

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

    return (q1, q2, q3)

if __name__ == "__main__":

    n = int(input())
    x = list(map(int, input().split(" ")))
    f = list(map(int, input().split(" ")))

    s = createFreqSet(x, f, n)

    q1 = getQuartils(s, len(s))[0]
    q3 = getQuartils(s, len(s))[2]

    print(q3 - q1)
