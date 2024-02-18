
N, M = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(N)]
select = []
chicken = []
house = []


def bt(start):
    global res
    if len(select) == M:
        sum = 0
        for x, y in house:
            dist = 2 * N
            for dx, dy in select:
                if abs(x - dx) + abs(y - dy) < dist:
                    dist = abs(x - dx) + abs(y - dy)
            sum += dist
        if sum < res:
            res = sum
            return

    for i in range(start, len(chicken)):
        select.append(chicken[i])
        bt(i + 1)
        select.pop()

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            house.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))
res = N * 2 * len(house)

bt(0)
print(res)