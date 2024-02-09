N, K = map(int, input().split())

def comb(n, k):
    if k == 1:
        return n
    elif k == 0 or k == n:
        return 1
    else:
        return comb(n - 1, k) + comb(n - 1, k - 1)
    
print(comb(N, K))