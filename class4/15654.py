N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []



def bt():
    if len(res) == M:
        print(*res)
        return
    for i in range(0, N):
        if arr[i] not in res:
            res.append(arr[i])
            bt()
            res.pop()

bt()
    


