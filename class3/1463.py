dp = [0 for i in range(1000001)]
N = int(input())

for i in range(2, 1000001):
    dp[i] = dp[i - 1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i // 2] + 1, dp[i])
    if i % 3 == 0:
        dp[i] = min(dp[i // 3] + 1, dp[i])


print(dp[N])