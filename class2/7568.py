N = int(input())

weight = [0 for _ in range(N)]

person = []
for _ in range(N):
    h, w = map(int, input().split())
    person.append((h, w))

for i in range(N):
    for j in range(i + 1, N):
        if person[i][0] > person[j][0] and person[i][1] > person[j][1]:
            weight[j] += 1
        elif person[i][0] < person[j][0] and person[i][1] < person[j][1]:
            weight[i] += 1

for rank in weight:
    print(rank + 1)

