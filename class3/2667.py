N = int(input())

home = [list(map(int, input())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]
res = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
house = 0

def dfs(x, y):
    global house
    visited[x][y] = 1
    house += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= N or nx < 0 or ny >= N or ny < 0:
            continue
        if home[nx][ny] == 1 and visited[nx][ny] != 1:
            dfs(nx, ny)

for i in range(N):
    for j in range(N):
        if home[i][j] == 1 and visited[i][j] != 1:
            dfs(i, j)
            res.append(house)
        house = 0

res.sort()
print(len(res))
for num in res:
    print(num)