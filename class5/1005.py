from collections import deque
T = int(input())

def bfs():
    while queue:
        q = queue.popleft()
        for n in build[q]:
            num[n] -= 1
            dp[n] = max(dp[n], dp[q] + arr[q - 1])
            if num[n] == 0:
                queue.append(n)

for _ in range(T):
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    num = [0] * (N + 1)
    dp = [0] * (N + 1)
    build = [[] for _ in range(N + 1)]
    queue = deque()

    for _ in range(K):
        a, b = map(int, input().split())
        build[a].append(b)
        num[b] += 1
    res = int(input())
    for i in range(1, N + 1):
        if num[i] == 0:
            queue.append(i)

    bfs()
    print(dp[res] + arr[res - 1])
