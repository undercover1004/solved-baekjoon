import sys
import heapq
N, M= map(int, input().split())
X = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b,c))

distance = [int(1e9)] * (N + 1)

def dijkstra():
    pq = []

    heapq.heappush(pq, (0, X))
    distance[X] = 0
    while pq:
        cnt, num = heapq.heappop(pq)
        if distance[num] < cnt:
            continue
        for x, y in graph[num]:
            cost = cnt + y
            if cost < distance[x]:
                distance[x] = cost
                heapq.heappush(pq, (cost, x))

dijkstra()
for i in range(1, N + 1):
    res = distance[i]
    if res >= int(1e9):
        print('INF')
    else:
        print(res)