N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == 1 and j == 1:
            dp[i][j] = arr[i - 1][j - 1]
        elif i == 1:
            dp[i][j] = dp[i][j - 1] + arr[i - 1][j - 1]
        elif j == 1:
            dp[i][j] = dp[i - 1][j] + arr[i - 1][j - 1]
        else:
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1] + arr[i - 1][j - 1]


for _ in range(M):
    a, b, c, d = map(int, input().split())
    res = dp[c][d] - dp[a - 1][d] - dp[c][b - 1] + dp[a - 1][b - 1]
    print(res)