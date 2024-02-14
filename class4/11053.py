N = int(input())
arr = list(map(int, input().split()))

dp = [1 for _ in range(N)]
res = 0

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
    res = max(res, dp[i])

print(res)