from collections import deque
start, end = map(int, input().split())
visited = [0 for _ in range(100001)]

def bfs(n):
    queue = deque()
    queue.append((n, 0))
    visited[n] = 1
    while queue:
        x, cnt = queue.popleft()
        if x == end:
            print(cnt)
            break
        if 2 * x <= 100000 and visited[2 * x] == 0:
            visited[2 * x] = 1
            queue.append((2 * x, cnt))
        if x - 1 >= 0 and visited[x - 1] == 0:
            visited[x - 1] = 1
            queue.append((x - 1, cnt + 1))
        if 1 + x <= 100000 and visited[1 + x] == 0:
            visited[1 +  x] = 1
            queue.append((1 + x, cnt + 1))

bfs(start)