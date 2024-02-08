N, M = map(int, input().split())


def Euclidean(a, b):
    while b != 0:
        [a, b] = [b, a%b]
    return a

result = Euclidean(N,M)
print(result)
print(int(N * M / result))