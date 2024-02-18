N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []


def bt(start):
    if len(res) == M:
        print(*res)
        return
    save = 0
    for i in range(start, N):
            if save != arr[i]:
                res.append(arr[i])
                save = arr[i]
                bt(i)
                res.pop()

bt(0)
    