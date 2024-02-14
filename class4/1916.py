import sys
import heapq

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

INF = int(1e9)
distance = [INF] * (N + 1)

def dijkstra(start, end):
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cnt, x = heapq.heappop(pq)
        if distance[x] < cnt:
            continue
        for y in graph[x]:
            cost = distance[x] + y[1]
            if distance[y[0]] > cost:
                distance[y[0]] = cost
                heapq.heappush(pq, (cost, y[0]))

    return distance[end]

start, end = map(int, input().split())
print(dijkstra(start, end))