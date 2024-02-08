while(True):
    stack = []
    mirror = True
    line = str(input())
    if line == '.':
        break
    for i in range(len(line)):
        if line[i] == '(' or line[i] == '[':
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
        elif line[i] == ']':
            if not stack:
                mirror = False
                break
            if stack.pop() == '[':
                continue
            else:
                mirror = False
                break
    if stack:
        mirror = False
    if mirror:
        print("yes")
    else:
        print("no")
