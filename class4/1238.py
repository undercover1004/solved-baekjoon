import sys
import heapq
N, M, X = map(int, input().split())


graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))


def dijkstra(start, end):
    pq = []
    distance = [[int(1e9)] * (N + 1) for _ in range(N + 1)]
    heapq.heappush(pq, (0, start))
    distance[start][start] = 0
    while pq:
        cnt, num = heapq.heappop(pq)
        if distance[start][num] < cnt:
            continue
        for x, y in graph[num]:
            cost = cnt + y
            if cost < distance[start][x]:
                distance[start][x] = cost
                heapq.heappush(pq, (cost, x))
    return distance[start][end]

res = 0
for i in range(1, N + 1):
    res = max(res, dijkstra(X, i) + dijkstra(i, X))

print(res)