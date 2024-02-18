V, E = map(int, input().split())

# 유니온 파인드
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
minus = 0
# 최소 스패닝 트리
# 부모가 같아질 때까지 작은 값 추가(같으면 무시)
for cnt, a, b in edge:
    if find(parent, a) == find(parent, b):
        continue
    union(parent, a, b)
    # 제일 큰 값 저장(분리할 곳 찾기)
    minus = max(cnt, minus)
    res += cnt

# 최소 스패닝 트리 - 분리할 곳
print(res - minus)