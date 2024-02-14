import sys
from collections import deque

N = int(sys.stdin.readline())
arr = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
result = 0
start = 0

for _ in range(N):
    tree = list(map(int, sys.stdin.readline().rstrip().split()))
    num = tree[0]
    i = 1
    while(tree[i] != -1):
        arr[num].append((tree[i], tree[i + 1]))
        i += 2

def bfs(x):
    global result, start
    queue = deque()
    queue.append((x, 0))
    visited[x] = 1
    while queue:
        num, cnt = queue.popleft()
        if cnt > result:
            result = cnt
            start = num
        for a, b in arr[num]:
            if visited[a] != 1:
                visited[a] = 1
                queue.append((a, cnt + b))


bfs(1)
visited = [0] * (N + 1)
bfs(start)
print(result)