import sys

arr = [[False for _ in range(2501)] for _ in range(2501)]
dp = [0 for _ in range(2501)]
string = sys.stdin.readline().rstrip()
string = " " + string
N = len(string)
for i in range(1, N):
    arr[i][i] = True

for i in range(N - 1):
    if string[i] == string[i + 1]:
        arr[i][i + 1] = True

for i in range(2, N):
    for j in range(1, N - i):
        if string[j] == string[j + i] and arr[j + 1][j + i - 1]:
            arr[j][j + i] = True

INF = int(1e9)
for i in range(1, N):
    dp[i] = INF
    for j in range(i + 1):
        if arr[j][i]:
            dp[i] = min(dp[i], dp[j - 1] + 1)

print(dp[N - 1])