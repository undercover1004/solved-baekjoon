N = int(input())


fx = []
for _ in range(N):
    x, y = map(int, input().split())
    fx.append((x, y))

fx.sort(key = lambda x:(x[0], x[1]))

for x, y in fx:
    print(x, y)