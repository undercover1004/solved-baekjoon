from collections import deque
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1 for _ in range(N)] for _ in range(N)]



eat = 0
res = 0
size = 2
queue = deque()
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def visit():
    for i in range(N):
        for j in range(N):
            visited[i][j] = -1

for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            queue.append((i, j))
            visited[i][j] = 0
            arr[i][j] = 0

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == -1 and arr[nx][ny] <= size:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1

def move():
    x, y = 0, 0
    dist = N * N
    for i in range(N):
        for j in range(N):
            if arr[i][j] < size and visited[i][j] != -1 and arr[i][j] != 0:
                if dist > visited[i][j]:
                    dist = visited[i][j]
                    x, y = i, j

    if dist == N * N:
        return False
    else:
        return x, y, dist

while(True):
    bfs()
    result = move()
    if not result:
        break
    i, j, dist = result[0], result[1], result[2]
    visit()
    eat += 1
    if size == eat:
        size += 1
        eat = 0
    arr[i][j] = 0
    visited[i][j] = 0
    queue.append((i, j))
    res += dist

print(res)