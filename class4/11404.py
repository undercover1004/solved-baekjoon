N = int(input())
M = int(input())

INF = int(1e9)
dp = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, input().split())
    dp[a][b] = min(dp[a][b], c)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            if i == j or j == k or k == i:
                continue
            dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
    dp[i][i] = 0

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if dp[i][j] == INF:
            dp[i][j] = 0

for num in dp[1:]:
    print(*num[1:])