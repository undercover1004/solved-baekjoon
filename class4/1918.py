stack = []

line = str(input())

for i in range(len(line)):
    s = line[i]
    if s == '(':
        stack.append(s)
    elif s == '+' or s == '-':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.append(s)
    elif s == '*' or s == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            print(stack.pop(), end='')
        stack.append(s)
    elif s == ')':
        while stack and stack[-1] != '(':
            print(stack.pop(), end='')
        stack.pop()
    else:
        print(s,end='')


while stack:
    print(stack.pop(),end='')