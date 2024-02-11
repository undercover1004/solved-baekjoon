dp = [1] * 1001

for i in range(2, 1001):
    dp[i] = (dp[i - 1] + dp[i - 2] * 2) % 10007

N = int(input())
print(dp[N])