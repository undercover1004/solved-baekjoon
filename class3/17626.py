dp = [10000] * 50001

N = int(input())
dp[1] = 1
for i in range(2, N + 1):
    for j in range(1, int(i ** 0.5) + 1):
        if j * j == i:
            dp[i] = 1
        else:
            dp[i] = min(dp[i], dp[i - j * j] + 1)

print(dp[N])