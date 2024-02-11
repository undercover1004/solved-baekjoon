T = int(input())

for _ in range(T):

    dict = {}

    N = int(input())
    for _ in range(N):
        a, b = map(str, input().split())
        if b in dict:
            dict[b] += 1
        else:
            dict[b] = 1

    result = 1
    for i in dict.values():
        result *= i + 1
    print(result - 1)