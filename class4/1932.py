N = int(input())

arr = [[0 for _ in range(N+1)] for _ in range(N+1)]
tri = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N + 1):
    k = list(map(int, input().split()))
    for j in range(1, i + 1):
        arr[i][j] = k[j - 1]

tri[1][1] = arr[1][1]

for i in range(1, N):
    for j in range(1, i + 1):
        tri[i + 1][j] = max(tri[i + 1][j], tri[i][j] + arr[i + 1][j])
        tri[i + 1][j + 1] = max(tri[i + 1][j + 1], tri[i][j] + arr[i + 1][j + 1])

res = 0
for num in tri[N]:
    res = max(num, res)
print(res)