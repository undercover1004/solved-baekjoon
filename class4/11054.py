N = int(input())
arr = list(map(int, input().split()))

dp1 = [1 for _ in range(N)]
dp2 = [1 for _ in range(N)]
res = 0

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i] and dp1[i] < dp1[j] + 1:
            dp1[i] = dp1[j] + 1


for i in range(N):
    for j in range(i):
        if arr[N - 1 - j] < arr[N - 1 - i] and dp2[N - 1 -i] < dp2[N - 1 - j] + 1:
            dp2[N - 1 - i] = dp2[N - 1 - j] + 1

for i in range(N):
    res = max(res, dp1[i] + dp2[i])

print(res - 1)