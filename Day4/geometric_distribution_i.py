
def geometric(n, p):
    return (1 - p) ** (n - 1) * p

if __name__ == '__main__':

    input_stream_1 = list(map(int, input().split(" ")))
    input_stream_2 = int(input())


    p = input_stream_1[0] / input_stream_1[1]
    n = input_stream_2

    result = geometric(n, p)

    print(round(result, 3))
    
