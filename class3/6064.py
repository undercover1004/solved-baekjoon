T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split())
    res = -1
    while(x <= M * N):
        if (x - y) % N == 0:
            res = x
            break
        x += M

    print(res)