N = int(input())
dp = [-1 for _ in range(N + 1)]
if N >= 3:
    dp[3] = 1
if N >= 5:
    dp[5] = 1

for i in range(6, N + 1):
    a = dp[i - 3]
    b = dp[i - 5]
    if a == -1 or b == -1:
        if a == -1 and b == -1:
            dp[i] = -1
        else:
            if a == -1:
                dp[i] = dp[i - 5] + 1
            elif b == -1:
                dp[i] = dp[i - 3] + 1
    else:
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1

print(dp[N])