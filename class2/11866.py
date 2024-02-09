N, K = map(int, input().split())
queue = []
for i in range(1, N + 1):
    queue.append(i)

result = []
idx = 0
while queue:
    idx += K - 1
    idx %= len(queue)
    result.append(str(queue.pop(idx)))

print("<", ", ".join(result), ">", sep="")