import sys
input = sys.stdin.readline
N, M = map(int, input().split())

dict = {}
for _ in range(N):
    a, b = input().split()
    dict[a] = b

for _ in range(M):
    a = input().rstrip()
    print(dict[a])