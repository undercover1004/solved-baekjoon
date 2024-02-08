N = int(input())
for _ in range(N):
    stack = []
    mirror = True
    line = str(input())
    if line == '.':
        break
    for i in range(len(line)):
        if line[i] == '(':
            stack.append(line[i])
        elif line[i] == ')':
            if not stack:
                mirror = False
                break
            if stack.pop() == '(':
                continue
            else:
                mirror = False
                break
    if stack:
        mirror = False
    if mirror:
        print("YES")
    else:
        print("NO")