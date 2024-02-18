A, B = map(int, input().split())

count = 1
while(True):
    if B % 10 == 1:
        B = B // 10
    else:
        B = B / 2
    count += 1
    
    if B == A:
        print(count)
        break
    elif B == 0:
        print(-1)
        break