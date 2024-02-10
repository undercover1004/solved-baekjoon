N, M = map(int, input().split())

maze = [list(map(int, input())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

queue = [(0, 0, 1)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
while(queue):
    q = queue.pop(0)
    x = q[0]
    y = q[1]
    cnt = q[2]
    if x == N - 1 and y == M - 1:
        print(cnt)
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue
        if visited[nx][ny] != 1 and maze[nx][ny] == 1:
            queue.append((nx, ny, cnt + 1))
            visited[nx][ny] = 1