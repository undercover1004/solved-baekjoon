import sys
T = int(input())

for _ in range(T):
    error = False
    flag = 0
    AC = str(input())
    n = int(input())
    arr = list(sys.stdin.readline().rstrip()[1:-1].split(","))
    if n == 0:
        arr = []
    for i in range(len(AC)):
        if AC[i] == 'R':
            flag += 1
        elif AC[i] == 'D':
            if arr:
                if flag % 2 == 0:
                    arr.pop(0)
                else:
                    arr.pop()
            else:
                print("error")
                error = True
                break
    if error == False:
        if flag % 2 != 0:
            arr.reverse()
        print("[", ",".join(arr), "]", sep="")
