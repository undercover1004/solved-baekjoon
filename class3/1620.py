N, M = map(int,input().split())
dict = {}

for i in range(1, N + 1):
    p = str(input())
    dict[i] = p
    dict[p] = i

for _ in range(M):
    ip = input()
    if ip.isdigit():
        print(dict[int(ip)])
    else:
        print(dict[ip])