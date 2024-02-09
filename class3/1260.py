from collections import deque
N, M, V = map(int, input().split())

graph = [[0 for _ in range(1001)] for _ in range(1001)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [0 for _ in range(1001)]

def dfs(i):
    print(i, end=" ")
    visited[i] = 1
    for j in range(1, N + 1):
        if graph[i][j] == 1 and visited[j] != 1:
            dfs(j)

def bfs():
    queue = deque()
    queue.append(V)
    visited[V] = 1
    while(queue):
        q = queue.popleft()
        print(q, end=" ")
        for j in range(1, N + 1):
            if graph[q][j] == 1 and visited[j] != 1:
                visited[j] = 1
                queue.append(j)

dfs(V)
visited = [0 for _ in range(1001)]
print()
bfs()