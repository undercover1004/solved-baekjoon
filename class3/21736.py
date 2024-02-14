import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

arr = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'I':
            queue.append((i, j))
            visited[i][j] == 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = 0
while queue:
    x, y = queue.popleft()
    if arr[x][y] == 'P':
        result += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] == 0 and arr[nx][ny] != 'X':
            visited[nx][ny] = 1
            queue.append((nx, ny))
if result:
    print(result)
else:
    print('TT')
