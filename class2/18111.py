N, M, B = map(int, input().split())

block = []
height = []
res = []
for _ in range (N):
    block.append(list(map(int, input().split())))


for i in range(N):
    for j in range(M):
        height.append(block[i][j])

def fill(h):
    global copyB
    time = 0
    for i in range(N):
        for j in range(M):
            if h > block[i][j]:
                time += (h - block[i][j])
                copyB -= (h - block[i][j])
            elif h < block[i][j]:
                time += 2 * (block[i][j] - h)
                copyB += (block[i][j] - h)
    if copyB >= 0:
        res.append((time, h))
for h in range(min(height), max(height) + 1):
    copyB = B
    fill(h)
res.sort(key = lambda x:(x[0], -x[1]))

print(res[0][0], res[0][1])
