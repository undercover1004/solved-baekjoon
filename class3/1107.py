import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
if M > 0:
    down = list(map(int, input().split()))
else:
    down = []

result = abs(N - 100)


queue = []

queue.append((N, pow(10, len(str(N)))))
while(queue):
    q = queue.pop()
    n = q[0]
    d = q[1]
    if d == 0:
        result = min(result, abs(n - N) + len(str(n)))
        continue
    num = (n % (d * 10)) // d
    n -= num * d
    if d > 1 and len(str(d)) > len(str(n)):
        queue.append((n, d // 10))
    for i in range(0, 10):
        if i in down:
            continue
        queue.append((n + i * d, d // 10))

print(result)