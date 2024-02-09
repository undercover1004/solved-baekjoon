import math
N = int(input())

diff = []

def rounds(n):
    ceil = math.ceil(n)
    trunc = math.trunc(n)
    if ceil - n <= n - trunc:
        return ceil
    else:
        return trunc

for _ in range(N):
    diff.append(int(input()))

diff.sort()
exc = rounds(N * 0.15)
res = 0

for i in range(exc, N - exc):
    res += diff[i]

if N == 0:
    print(0)
else:
    print(rounds(res / (N - 2 * exc)))