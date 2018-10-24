import math

if __name__ == '__main__':

    # sample_size = int(input())
    # mean = float(input())
    # std = float(input())
    # interval = float(input())
    # z = float(input())

    sample_size = 100
    mean = 500
    std = 80
    interval = .95
    z = 1.96

    margin = z * std / math.sqrt(sample_size)
    lower_limit = mean - margin
    upper_limit = mean + margin

    print(round(lower_limit, 2))
    print(round(upper_limit, 2))
