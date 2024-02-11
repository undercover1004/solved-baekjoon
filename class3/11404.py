from collections import deque
N = int(input())

graph = [list(map(int, input().split())) for _ in range(N)]



for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][k] == 0 and graph[j][i] == 1 and graph[i][k] == 1:
                graph[j][k] = 1

for line in graph:
    print(*line)