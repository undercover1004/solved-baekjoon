import math
N = int(input())
fac = math.factorial(N)
fac = str(fac)[::-1]

cnt = 0
for i in range(len(fac)):
    if fac[i] == '0':
        cnt += 1
    else:
        break

print(cnt)