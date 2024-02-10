import sys
from collections import deque
M, N= map(int, input().split())

tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
queue = deque()

for j in range(N):
    for k in range(M):
        if tomato[j][k] == 1:
            queue.append((j, k))

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]

result = 0
while(queue):
    x, y = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if tomato[nx][ny] == 0:
            tomato[nx][ny] = tomato[x][y] + 1
            queue.append((nx, ny))

check = False
for j in range(N):
    for k in range(M):
        if tomato[j][k] == 0:
            print(-1)
            exit(0)
        else:
            result = max(result, tomato[j][k])

print(result - 1)