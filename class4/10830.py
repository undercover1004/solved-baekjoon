import sys
N, M = map(int, sys.stdin.readline().split())
num = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def recur(N, M):
    if M == 1:
        return N

    if M % 2 == 0:
        x = recur(N, M / 2)
        return multi(x, x)
    else:
        x = recur(N, (M - 1) / 2)
        return multi(multi(x,x), N)
    
def multi(x, y):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += x[i][k] * y[k][j]
                result[i][j] %= 1000
    return result


res = recur(num, M)
for i in range(N):
    for j in range(N):
        print(res[i][j] % 1000, end=' ')
    print()