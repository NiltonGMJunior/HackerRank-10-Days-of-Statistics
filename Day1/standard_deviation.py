def mean(x, n):
    return sum(x)/n

def variance(x, n):
    return sum(map(lambda x_i : (x_i - mean(x, n))**2, x))

def stdDev(x, n):
    return round((variance(x,n)/n)**(1/2), 1)

if __name__ == "__main__":

    n = int(input())
    x = list(map(int, input().split(" ")))

    print(stdDev(x,n))
