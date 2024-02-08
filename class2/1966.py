from collections import deque
N = int(input())
sequence = []
for _ in range(N):
    M, K = map(int, input().split())
    p = list(map(int, input().split()))
    queue = deque()
    for i in range(len(p)):
        queue.append((i, p[i]))
    result = 1
    
    while(True):
        big = max(queue, key=lambda x: x[1])[1]
        num = queue.popleft()
        if num[1] < big:
            queue.append(num)
        elif num[1] == big:
            if num[0] == K:
                sequence.append(result)
                break
            result += 1
for s in sequence:
    print(s)
        
