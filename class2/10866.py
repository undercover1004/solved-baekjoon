import sys
from collections import deque
N = int(sys.stdin.readline())
stack = deque()
for _ in range(N):
    s = sys.stdin.readline().split()
    if s[0] == 'push_front':
        stack.appendleft(int(s[1]))
    elif s[0] == 'push_back':
        stack.append(int(s[1]))
    elif s[0] == 'pop_front':
        if not stack:
            print(-1)
        else:
            print(stack.popleft())
    elif s[0] == 'pop_back':
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
