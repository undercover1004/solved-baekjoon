N = int(input())
dp = [[0,0] for _ in range(41)]
dp[0][0] = 1
dp[0][1] = 0
dp[1][1] = 1
dp[1][0] = 0
num = []
for i in range(2, 41):
    for j in range(2):
        dp[i][j] = dp[i - 1][j] + dp[i - 2][j]

for _ in range(N):
    num.append(int(input()))

for n in num:
    print(dp[n][0], dp[n][1])