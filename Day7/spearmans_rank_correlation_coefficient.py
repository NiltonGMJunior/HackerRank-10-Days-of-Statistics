if __name__ == '__main__':

    # n = int(input())
    # X = list(map(float, input().split()))
    # Y = list(map(float, input().split()))

    n = int('10')
    X = list(map(float, "10 9.8 8 7.8 7.7 1.7 6 5 1.4 2".split()))
    Y = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))

    sort_X = [elem_x for elem_x in X]
    sort_X.sort()
    sort_Y = [elem_y for elem_y in Y]
    sort_Y.sort()

    X_rX = dict([(index + 1, elem_X) for index, elem_X in enumerate(sort_X)])
    Y_rY = dict([(index + 1, elem_Y) for index, elem_Y in enumerate(sort_Y)])

    d = []

    for k in range(1, n + 1):
        r_X = k
        elem_X = X_rX[r_X]
        elem_Y = Y[X.index(elem_X)]
        r_Y = sort_Y.index(elem_Y) + 1
        d.append((r_Y - r_X) ** 2)

    r_XY = 1 - 6 * sum(d) / n / (n ** 2 - 1)

    print(round(r_XY, 3))
