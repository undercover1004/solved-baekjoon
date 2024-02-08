while(True):
    line = list(map(int, input().split()))
    line.sort(reverse=True)
    if line[0] == 0 and line[1] == 0 and line[2] == 0:
        break
    if line[0] ** 2 == line[1] ** 2 + line[2] ** 2:
        print("right")
    else:
        print("wrong")