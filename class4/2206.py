import sys
from collections import deque
N, M = map(int, input().split())

arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(2)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    queue = deque()
    queue.append((0, 0, 0, 1))
    visited[0][0][0] = 1
    while queue:
        x, y, cnt, res = queue.popleft()
        if x == N - 1 and y == M - 1:
            return res
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if cnt == 0 and arr[nx][ny] == 1:
                visited[1][nx][ny] = 1
                queue.append((nx, ny, 1, res + 1))
            else:
                if visited[cnt][nx][ny] == 0 and arr[nx][ny] == 0:
                    visited[cnt][nx][ny] = 1
                    queue.append((nx, ny, cnt, res + 1))
    return -1

print(bfs())