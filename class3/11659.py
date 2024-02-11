N, M = map(int, input().split())
num = list(map(int, input().split()))
dp = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    dp[i] = dp[i - 1] + num[i - 1]

for _ in range(M):
    x, y = map(int, input().split())
    print(dp[y] - dp[x - 1])
   