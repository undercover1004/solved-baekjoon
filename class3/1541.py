import sys
line = sys.stdin.readline()


minus = False
result = 0
num = ""
for i in range(len(line)):
    if line[i] == '+' or line[i] == '-' or line[i] == '\n':
        if minus:
            result -= int(num)
        else:
            result += int(num)
        if line[i] == '-':
            minus = True
        num = ""
    else:
        num += line[i]

print(result)

