N, M = map(int, input().split())


lie = list(map(int, input().split()))[1:]
truth = set(lie)

parent = [i for i in range(N + 1)]
party = []

def find(parent, x):
    if x != parent[x]:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a in truth and b in truth:
        return
    if a in truth:
        parent[b] = a
    elif b in truth:
        parent[a] = b
    else:
        if a > b:
            parent[a] = b
        else:
            parent[b] = a

for j in range(M):
    arr = list(map(int, input().split()))[1:]
    for i in range(1, len(arr)):
        union(arr[i - 1], arr[i])
    party.append(arr)

res = 0
for p in party:
    check = False
    for num in p:
        if find(parent, num) in truth:
            check = True
            break
    if not check:
        res += 1

print(res)
