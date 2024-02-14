N = int(input())

queen = [0] * N
res = 0

def promising(j):
    for i in range(j):
        if queen[i] == queen[j] or abs(i - j) == abs(queen[i] - queen[j]):
            return False
    return True

def nqueen(x):
    global res
    if x == N:
        res += 1
        return
    for i in range(1, N + 1):
        queen[x] = i
        if promising(x):
            nqueen(x + 1)

nqueen(0)
print(res)