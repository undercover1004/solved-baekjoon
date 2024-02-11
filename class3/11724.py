from collections import deque
N, M = map(int, input().split())

graph = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(i):
    queue = deque()
    queue.append(i)
    visited[i] = 1
    while(queue):
        q = queue.popleft()
        for num in graph[q]:
            if visited[num] != 1:
                visited[num] = 1
                queue.append(num)

result = 0
visited = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    if visited[i] != 1:
        bfs(i)
        result += 1

print(result)