import sys
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == 'push':
        stack.append(int(s[1]))
    elif s[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif s[0] == 'size':
        print(len(stack))
    elif s[0] == 'front':
        if not stack:
            print(-1)
        else:
            print(stack[0])
    elif s[0] == 'back':
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif s[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
