import sys
import math
N= int(sys.stdin.readline())
K = 1000000007


def recur(N, M):
    if M == 1:
        return N % K
    if M % 2 == 0:
        x = recur(N, M / 2)
        return x * x % K
    else:
        x = recur(N, (M - 1) / 2)
        return x * x * N % K
    
res = 0
for _ in range(N):
    b, a = map(int, input().split())
    gcd = math.gcd(a, b)
    b = b // gcd
    a = a // gcd
    res += a * recur(b, K - 2) % K
    res %= K
print(res)