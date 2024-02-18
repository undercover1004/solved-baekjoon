r, c, t = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(r)]
save = [[0 for _ in range(c)] for _ in range(r)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def dust():
    queue = []
    for i in range(r):
        for j in range(c):
            if arr[i][j] > 0:
                queue.append((i, j))

    while queue:
        x, y = queue.pop()
        cnt = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c and arr[nx][ny] != -1:
                cnt += 1
                save[nx][ny] += arr[x][y] // 5
        arr[x][y] -= (arr[x][y] // 5) * cnt
    
    for i in range(r):
        for j in range(c):
            arr[i][j] += save[i][j]
            save[i][j] = 0

air = []
def condition():
    x, y = air[0]
    for i in range(x - 1, -1, -1):
        arr[i][y] = arr[i - 1][y]
    for j in range(y, c - 1):
        arr[0][j] = arr[0][j + 1]
    for i in range(0, x + 1):
        arr[i][c - 1] = arr[i + 1][c - 1]
    for j in range(c - 1, y + 1, -1):
        arr[x][j] = arr[x][j - 1]
    arr[x][y + 1] = 0
    x, y = air[1]
    for i in range(x + 1, r - 1):
        arr[i][y] = arr[i + 1][y]
    for j in range(y, c - 1):
        arr[r - 1][j] = arr[r - 1][j + 1]
    for i in range(r - 1, x, -1):
        arr[i][c - 1] = arr[i - 1][c - 1]
    for j in range(c - 1, y + 1, -1):
        arr[x][j] = arr[x][j - 1]
    arr[x][y + 1] = 0

def sum():
    res = 0
    for i in range(r):
        for j in range(c):
            if arr[i][j] != -1:
                res += arr[i][j]
    return res

for i in range(r):
    for j in range(c):
        if arr[i][j] == -1:
            air.append((i, j))

for _ in range(t):
    dust()
    condition()
print(sum())