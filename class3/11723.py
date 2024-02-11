import sys
N = int(input())

arr = set()
for _ in range(N):
    x = sys.stdin.readline().split()
    if x[0] == 'add':
        arr.add(int(x[1]))
    elif x[0] == 'remove':
        arr.discard(int(x[1]))
    elif x[0] == 'check':
        if int(x[1]) in arr:
            print(1)
        else:
            print(0)
    elif x[0] == 'toggle':
        if int(x[1]) in arr:
            arr.remove(int(x[1]))
        else:
            arr.add(int(x[1]))
    elif x[0] == 'all':
        arr.update({1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20})
    elif x[0] == 'empty':
        arr = set()