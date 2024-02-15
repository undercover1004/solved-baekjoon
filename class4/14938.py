import heapq
N, M, R = map(int, input().split())


INF = int(1e9)
item = list(map(int, input().split()))
distance = [INF] * (N + 1)
graph = [[] for _ in range(N + 1)]

for _ in range(R):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance[start] = 0
    pq = []
    heapq.heappush(pq, (0, start))
    while pq:
        cnt, x = heapq.heappop(pq)
        if distance[x] < cnt:
            continue
        for y in graph[x]:
            cost = y[1] + distance[x]
            if distance[y[0]] > cost:
                distance[y[0]] = cost
                heapq.heappush(pq, (cost, y[0]))
    sum = 0
    for i in range(1, N + 1):
        if distance[i] <= M:
            sum += item[i - 1]
    return sum
    
res = 0
for i in range(1, N + 1):
    distance = [INF] * (N + 1)
    res = max(res, dijkstra(i))

print(res)