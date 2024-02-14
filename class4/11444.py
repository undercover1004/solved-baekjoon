import sys
N = int(sys.stdin.readline())
fibo = [[1, 1], [1, 0]]

def fibonacci(n, fibo):
    if n == 1:
        return fibo
    
    x = fibonacci(n // 2, fibo)
    if n % 2 == 0:
        return multi(x, x)
    else:
        return multi(multi(x, x), fibo)
    
def multi(x, y):
    N = len(x)
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            num = 0
            for k in range(N):
                num += x[i][k] * y[k][j]
            result[i][j] = num % 1000000007
    return result

print(fibonacci(N, fibo)[0][1])