N, M = map(int, input().split())
res = []



def bt(start):
    if len(res) == M:
        print(*res)
        return
    for i in range(start, N + 1):
        res.append(i)
        bt(i)
        res.pop()

bt(1)
    


