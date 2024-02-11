import heapq, sys

N = int(input())
pq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if pq:
            print(-heapq.heappop(pq))
        else:
            print(0)
    else:
        heapq.heappush(pq, -x)

