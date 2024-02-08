N = int(input())
num = []
for _ in range(N):
    n = int(input())
    num.append(n)
num.sort()
for n in num:
    print(n)