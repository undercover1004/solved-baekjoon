N, M = map(int, input().split())

visited = [0 for _ in range(100001)]

queue = [(N, 0)]
visited[N] = 1
while(queue):
    q = queue.pop(0)
    x = q[0]
    cnt = q[1]
    if x == M:
        print(cnt)
        break
    if x + 1 <= 100000:
        if visited[x + 1] != 1:
            queue.append((x + 1, cnt + 1))
            visited[x + 1] = 1
    if x - 1 >= 0:
        if visited[x - 1] != 1:
            queue.append((x - 1, cnt + 1))
            visited[x - 1] = 1
    if (2 * x) <= 100000:
        if visited[x * 2] != 1:
            queue.append((2 * x, cnt + 1))
            visited[x * 2] = 1


