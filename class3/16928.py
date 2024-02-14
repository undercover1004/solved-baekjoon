from collections import deque
snake = [0 for _ in range(101)]
visited = [0 for _ in range(101)]
N, M = map(int, input().split())

queue = deque()
queue.append((1, 0))
visited[1] = 1

for _ in range(N + M):
    a, b = map(int, input().split())
    snake[a] = b

while queue:
    q, cnt = queue.popleft()
    if q == 100:
        print(cnt)
    for i in range(1, 7):
        num = q + i
        if num > 100:
            continue
        if snake[num] and visited[num] != 1:
            visited[num] = 1
            visited[snake[num]] = 1
            queue.append((snake[num], cnt + 1))
        else:
            if visited[num] != 1:
                visited[num] = 1
                queue.append((num, cnt + 1))
            