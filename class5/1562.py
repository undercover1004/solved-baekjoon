N = int(input())
dp = [[[0] * (1 << 10) for _ in range(10)] for _ in range(N + 1)]
MOD = 1000000000

for i in range(10):
    dp[1][i][1 << i] = 1

for i in range(2, N + 1):
    for j in range(10):
        for k in range(1 << 10):
            if j < 9 :
                dp[i][j][k | 1 << j] += dp[i - 1][j + 1][k]
                dp[i][j][k | 1 << j] %= MOD
            if j > 0:
                dp[i][j][k | 1 << j] += dp[i - 1][j - 1][k]
                dp[i][j][k | 1 << j] %= MOD

res = 0
for i in range(1, 10):
    res += dp[N][i][0b1111111111]
    res %= MOD

print(res)