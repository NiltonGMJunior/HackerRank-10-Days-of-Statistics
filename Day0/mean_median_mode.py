
def mean(v, n):
    return sum(v)/n

def median(v):
    v.sort()
    while True:
        if len(v) <= 2:
            return mean(v, len(v))
        v = v[1:-1]

def mode(v):
    value_counts = {}
    for element in v:
        if element not in value_counts:
            value_counts[element] = 1
        else:
            value_counts[element] += 1

    values = []

    for key in value_counts:
        values.append((key,value_counts[key]))

    max_value = max([counts for elem, counts in values])

    return min([elem for elem, counts in values if counts == max_value])


if __name__ == "__main__":

    #n = int(input())
    #v = list(map(int, input().split()))

    n = int('10')
    v = list(map(int, '64630 11735 14216 99233 14470 4978 73429 38120 51135 67060'.split()))

    print(mean(v, n))
    print(median(v))
    print(mode(v))
