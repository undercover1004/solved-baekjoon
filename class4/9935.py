string = str(input())
bomb = str(input())
k = len(bomb)
stack = []

for i in string:
    stack += i
    while stack[-k::] == [*bomb]:
        del stack[-k::]
if stack == []:
    print("FRULA")
else:
    print("".join(stack))