M, N = map(int, input().split())

def odd(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1 ):
        if n % i == 0:
            return False
    return True
    
for i in range(M, N+1):
    if odd(i):
        print(i)