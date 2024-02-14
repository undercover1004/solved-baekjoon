from collections import deque
N = int(input())

arr = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visited = [0 for _ in range(N + 1)]
visited[1] = 1
queue = deque()
queue.append(1)
while queue:
    num = queue.popleft()
    for kid in arr[num]:
        if visited[kid] == 0:
            visited[kid] = num
            queue.append(kid)

for i in range(2, N + 1):
    print(visited[i])