N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []



def bt(start):
    if len(res) == M:
        print(*res)
        return
    for i in range(start, N):
            res.append(arr[i])
            bt(i)
            res.pop()

bt(0)
    