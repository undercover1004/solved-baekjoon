import sys
N = int(sys.stdin.readline().rstrip())

count = [0 for _ in range(10001)]

for _ in range(N):
    n = int(sys.stdin.readline().rstrip())
    count[n] += 1

for i in range(10001):
    for _ in range(count[i]):
        print(i)
