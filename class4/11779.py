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
parent = [0] * (N + 1)
start, end = map(int, input().split())

def dijkstra(start):
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
                parent[y[0]] = x
                heapq.heappush(pq, (cost, y[0]))

  
dijkstra(start)

it = end
path = [end]
while it != start:
    it = parent[it]
    path.append(it)

print(distance[end])
print(len(path))
path.reverse()
print(' '.join(map(str,path)))