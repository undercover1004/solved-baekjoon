from collections import deque
T = int(input())



for _ in range(T):
    visited = [0] * 10001
    queue = deque()
    A, B = map(int, input().split())
    queue.append((A, ""))
    visited[A] = 1
    while(queue):
        q = queue.popleft()
        num = q[0]
        result = q[1]
        if num == B:
            print(result)
            break
        left = num // 1000 + (num % 1000) * 10
        right = num // 10 + (num % 10) * 1000
        if num == 0:
            S = 9999
        else:
            S = num - 1
        D = (num * 2 % 10000)
        if visited[left] != 1:
            visited[left] = 1
            queue.append((left, result + 'L'))
        if visited[right] != 1:
            visited[right] = 1
            queue.append((right, result + 'R'))
        if visited[S] != 1:
            visited[S] = 1
            queue.append((S, result + 'S'))
        if visited[D] != 1:
            visited[D] = 1
            queue.append((D, result + 'D'))

