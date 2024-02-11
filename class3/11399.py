import heapq
N = int(input())


pq = list(map(int, input().split()))
heapq.heapify(pq)

result = 0
while pq:
    result += N * heapq.heappop(pq)
    N -= 1

print(result)