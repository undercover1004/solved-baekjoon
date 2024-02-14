import sys
N, M, K = map(int, sys.stdin.readline().split())

def recur(N, M):
    if M == 1:
        return N % K
    if M % 2 == 0:
        x = recur(N, M / 2)
        return x * x % K
    else:
        x = recur(N, (M - 1) / 2)
        return x * x * N % K
    
print(recur(N, M))