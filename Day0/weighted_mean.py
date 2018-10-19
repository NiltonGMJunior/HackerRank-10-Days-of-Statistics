def weighted_mean(n, x, w):
    return round(sum([elem_x*elem_w for elem_x, elem_w in zip(x, w)])/sum(w),1)

if __name__ == "__main__":

    # n = int(input())
    # x = list(map(int, input().split(" ")))
    # w = list(map(int, input().split(" ")))

    n = int('10')
    x = list(map(int, '10 40 30 50 20 10 40 30 50 20'.split(" ")))
    w = list(map(int, '1 2 3 4 5 6 7 8 9 10'.split(" ")))

    print(weighted_mean(n, x, w))
