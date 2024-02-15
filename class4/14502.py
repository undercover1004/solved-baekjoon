from collections import deque
import copy

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
queue = deque()

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
res = 0


def bfs():
    global res
    copy_arr = copy.deepcopy(arr)
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 2:
                queue.append((i, j))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if copy_arr[nx][ny] == 0:
                copy_arr[nx][ny] = 2
                queue.append((nx, ny))
    count = 0
    for i in range(N):
        for j in range(M):
            if copy_arr[i][j] == 0:
                count += 1
    res = max(res, count)
    
def wall(n):
    if n == 3:
        bfs()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(n + 1)
                arr[i][j] = 0

wall(0)
print(res)