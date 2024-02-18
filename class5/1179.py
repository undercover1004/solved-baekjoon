V, E = map(int, input().split())

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

edge = []
parent = [i for i in range(V + 1)]
for _ in range(E):
    a, b, cnt = map(int, input().split())
    edge.append((cnt, a, b))

edge.sort()
res = 0
for cnt, a, b in edge:
    if find(parent, a) == find(parent, b):
        continue
    union(parent, a, b)
    res += cnt

print(res)