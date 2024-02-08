N = int(input())
stk = []
result = []

num = 1
fail = False

for _ in range(N):
    cnt = int(input())
    if not stk:
        stk.append(num)
        num += 1
        result.append('+')
    if stk[-1] > cnt:
        fail = True
        break
    if stk[-1] < cnt:
        while(stk[-1] < cnt):
            stk.append(num)
            result.append('+')
            num += 1
    if stk[-1] == cnt:
        result.append('-')
        stk.pop()


if fail:
    print("NO")
else:
    for word in result:
        print(word)
