from collections import deque
N = int(input())

rgb = [list(map(str, input())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(i, j, rg):
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    while(queue):
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= N or nx < 0 or ny >= N or ny < 0:
                continue
            if rg:
                if rgb[x][y] == 'B':
                    if rgb[x][y] == rgb[nx][ny] and visited[nx][ny] != 1:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
                else:
                    if rgb[nx][ny] != 'B' and visited[nx][ny] != 1:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))
            else:
                if rgb[nx][ny] == rgb[x][y] and visited[nx][ny] != 1:
                        visited[nx][ny] = 1
                        queue.append((nx, ny))

res1, res2 = 0, 0
for i in range(N):
    for j in range(N):
        if visited[i][j] != 1:
            bfs(i, j, False)
            res1 += 1

visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visited[i][j] != 1:
            bfs(i, j, True)
            res2 += 1

print(res1, res2, sep='\n')
            

