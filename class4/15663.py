import copy
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []


def bt():
    if len(res) == M:
        for num in res:
             print(arr[num], end=" ")
        print()
        return
    save = 0
    for i in range(0, N):
            if i not in res and save != arr[i]:
                res.append(i)
                save = arr[i]
                bt()
                res.pop()

bt()
    