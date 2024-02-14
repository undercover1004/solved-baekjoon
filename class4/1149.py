N = int(input())

dp = [[0 for _ in range(3)] for _ in range(N)]

paint = [list(map(int, input().split())) for _ in range(N)]

for i in range(3):
    dp[0][i] = paint[0][i]
for i in range(1, N):
    dp[i][0] = min(dp[i - 1][1] + paint[i][0], dp[i - 1][2] + paint[i][0])
    dp[i][1] = min(dp[i - 1][0] + paint[i][1], dp[i - 1][2] + paint[i][1])
    dp[i][2] = min(dp[i - 1][0] + paint[i][2], dp[i - 1][1] + paint[i][2])



print(min(dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]))