N = int(input())

dp = [[0 for _ in range(2)] for _ in range(301)]

stair = [int(input()) for _ in range(N)]

if N >= 2:
    dp[1][0] = stair[0]
    dp[2][1] = stair[1] + stair[0]
    dp[2][0] = stair[1]
else:
    print(stair[0])


for i in range(3, N + 1):
    dp[i][1] = dp[i - 1][0] + stair[i - 1]
    dp[i][0] = max(dp[i - 2][0], dp[i - 2][1]) + stair[i - 1]

if N != 1:
    print(max(dp[N][0], dp[N][1]))