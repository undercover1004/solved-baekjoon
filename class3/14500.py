import sys
N, M = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = -1

# dfs 활용
def dfs(x, y, cnt, res):
    global result
    if cnt == 4:
        result = max(result, res)
        return
    elif result >= res + max_val * (4 - cnt):
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] != 1:
            visited[nx][ny] = 1
            if cnt == 2:
                # 2개가 채워졌을때 원점을 기준으로 넣음
                # 화살표 모양
                dfs(x, y, cnt + 1, res + arr[nx][ny])
            # dfs를 활용하여 화살표를 제외한 모든모양
            dfs(nx, ny, cnt + 1, res + arr[nx][ny])
            visited[nx][ny] = 0

max_val = max(map(max, arr))
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = 0

print(result)