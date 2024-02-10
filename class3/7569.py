import sys
from collections import deque
M, N, H = map(int, input().split())

tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
queue = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append((i, j, k))

dx = [1, 0, -1, 0, 0, 0]
dy = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

result = 0
while(queue):
    x, y, z = queue.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]
        if nx >= H or nx < 0 or ny >= N or ny < 0 or nz >= M or nz < 0:
            continue
        if tomato[nx][ny][nz] == 0:
            tomato[nx][ny][nz] = tomato[x][y][z] + 1
            queue.append((nx, ny, nz))

check = False
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            else:
                result = max(result, tomato[i][j][k])

print(result - 1)