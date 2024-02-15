from collections import deque
N, K = map(int, input().split())

visited = [0] * 100001
res = 0


result = int(1e9)
queue = deque()
queue.append((N, 0))
visited[N] = 1
while queue:
    n, cnt = queue.popleft()
    visited[n] = 1
    if n == K:
        visited[K] = 0
        if result < cnt:
            break
        result = cnt
        res += 1
    if 0 <= n + 1 and n + 1 <= 100000 and visited[n + 1] != 1:
        queue.append((n + 1, cnt + 1))
    if 0 <= n - 1 and n - 1 <= 100000 and visited[n - 1] != 1:
        queue.append((n - 1, cnt + 1))
    if 0 <= n * 2 and n * 2 <= 100000 and visited[n * 2] != 1:
        queue.append((n * 2, cnt + 1))

print(result)
print(res)