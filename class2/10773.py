N = int(input())
stack = []
for _ in range(N):
    num = int(input())
    if num == 0:
        stack.pop()
    else:
        stack.append(num)

sum = 0
for num in stack:
    sum += num
print(sum)