import heapq, sys

N = int(input())
pq = []
for _ in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if pq:
            num = heapq.heappop(pq)
            if num[1] == -1:
                print(-num[0])
            else:
                print(num[0])
        else:
            print(0)
    else:
        if x < 0:
            heapq.heappush(pq, (-x, -1))
        else:
            heapq.heappush(pq, (x, 0))

