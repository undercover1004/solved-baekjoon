import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
res = [[-1 for _ in range(M)]  for _ in range(N)]
queue = deque()

for i in range(N):
    for j in range(M):
        if board[i][j] == 2:
            queue.append((i, j))
            res[i][j] = 0
            visited[i][j] = True
        if board[i][j] == 0:
            res[i][j] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= M:
            continue
        if not visited[nx][ny] and board[nx][ny] == 1:
            queue.append((nx, ny))
            visited[nx][ny] = True
            res[nx][ny] = res[x][y] + 1
            

for line in res:
    print(*line)

