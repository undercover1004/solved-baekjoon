R, C = map(int, input().split())

arr = [list(map(str, input())) for _ in range(R)]
visited = [0] * 28

res = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, cnt):
    global res
    res = max(res, cnt)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= R or ny < 0 or ny >= C:
            continue
        if visited[ord(arr[nx][ny]) - 65] != 1:
            visited[ord(arr[nx][ny]) - 65] =1
            dfs(nx, ny, cnt + 1)
            visited[ord(arr[nx][ny]) - 65] = 0

visited[ord(arr[0][0]) - 65] = 1
dfs(0, 0, 1)
print(res)