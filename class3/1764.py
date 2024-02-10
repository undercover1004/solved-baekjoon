N, M = map(int, input().split())

notsee = set()
dbj = []

for _ in range(N):
    notsee.add(str(input()))

for _ in range(M):
    s = str(input())
    if s in notsee:
        dbj.append(s)

dbj.sort()
print(len(dbj))
for s in dbj:
    print(s)