N = int(input())
M = int(input())
graph = [[0 for _ in range(101)] for _ in range(101)]
visited = [0 for _ in range(101)]
result = 0


for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

queue = [1]
visited[1] = 1
while(queue):
    q = queue.pop(0)
    for i in range(1, N + 1):
        if visited[i] != 1 and graph[i][q] == 1:
            queue.append(i)
            result += 1
            visited[i] = 1

print(result)