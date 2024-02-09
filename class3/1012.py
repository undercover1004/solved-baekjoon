import sys
sys.setrecursionlimit(10**6)
T = int(input())

dp = [[0 for _ in range(50)] for _ in range(50)]
visited = [[0 for _ in range(50)] for _ in range(50)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def comb(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= M or ny < 0:
            continue
        if visited[nx][ny] != 1 and dp[nx][ny] == 1:
            comb(nx, ny)


def clear():
    for i in range(50):
        for j in range(50):
            dp[i][j] = 0
            visited[i][j] = 0

for _ in range(T):
    M, N, K = map(int, input().split())
    result = 0
    
    for _ in range(K):
        x, y = map(int, input().split())
        dp[y][x] = 1

    for i in range(N):
        for j in range(M):
            if dp[i][j] == 1 and visited[i][j] != 1:
                print((i, j))
                comb(i, j)
                result += 1

    print(result)
    clear()
