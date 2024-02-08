N, M = map(int, input().split())

num = list(map(int, input().split()))

result = 0
def black(idx, cnt, jack):
    global result
    
    if cnt == 3:
        if result <= jack and jack <= M:
            result = jack

    
    else:
        if N - idx < 3 - cnt:
            return
        black(idx + 1, cnt + 1, jack + num[idx])
        black(idx + 1, cnt, jack)


black(0, 0, 0)
print(result)