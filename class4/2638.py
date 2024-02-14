from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cheese = [[0 for _ in range(M)] for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append((0, 0))
    visited[0][0] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == 0:
                if arr[nx][ny] == 1:
                    cheese[nx][ny] += 1
                else:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

def melt():
    for i in range(N):
        for j in range(M):
            if cheese[i][j] >= 2:
                arr[i][j] = 0

def check():
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                return False
    return True

def reset():
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0
            cheese[i][j] = 0

res = 0
while(True):
    res += 1
    bfs()
    melt()
    if check():
        print(res)
        break
    reset()
