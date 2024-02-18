import heapq
N, K = map(int, input().split())

pq = []
pqk = []
for _ in range(N):
    m, v = map(int, input().split())
    heapq.heappush(pq, (m, v))

for _ in range(K):
    c = int(input())
    heapq.heappush(pqk, c)

res = 0
sum = []
while pqk:
    num = heapq.heappop(pqk)
    while pq and pq[0][0] <= num:
        heapq.heappush(sum, (-heapq.heappop(pq)[1]))
    if sum:
        res -= heapq.heappop(sum)
print(res)