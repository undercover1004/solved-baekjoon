import heapq
N, M = map(int, input().split())

arr = [[] for _ in range(N + 1)]
num = [0 for _ in range(N + 1)]
pq = []
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    num[b] += 1

for i in range(1, N + 1):
    if num[i] == 0:
        heapq.heappush(pq, i)

while pq:
    n = heapq.heappop(pq)
    print(n,end="")
    for cnt in arr[n]:
        num[cnt] -= 1
        if num[cnt] == 0:
            heapq.heappush(pq, cnt)