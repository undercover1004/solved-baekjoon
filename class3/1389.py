N, M = map(int, input().split())
friends = [[] for _ in range(N + 1)]
visited = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
result = [0 for _ in range(N)]

for _ in range(M):
    a, b = map(int,input().split())
    friends[a].append(b)
    friends[b].append(a)

def bfs(n):
    queue = [(n, 1)]
    while(queue):
        num = queue.pop(0)
        x = num[0]
        cnt = num[1]
        for f in friends[x]:
            if visited[n][f] != 1 and n != f:
                visited[n][f] = 1
                result[n - 1] += cnt
                queue.append((f, cnt + 1))

for i in range(1, N + 1):
    bfs(i)

for i in range(len(result)):
    if result[i] == min(result):
        print(i + 1)
        break
