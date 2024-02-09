N, r, c = map(int, input().split())

result = 0
def z(n, y, x):
    global result
    l = pow(2, n - 1)
    if l == 1:
        if x == 0 and y == 1:
            result += 2
        elif x == 1 and y == 0:
            result += 1
        elif x == 1 and y == 1:
            result += 3
        return
    if x >= l and y >= l:
        result += 3 * pow(4, n - 1)
        z(n - 1, y - l, x - l)
    elif x >= l and y < l:
        result += pow(4, n - 1)
        z(n - 1, y, x - l)
    elif x < l and y >= l:
        result += 2 * pow(4, n - 1)
        z(n - 1, y - l, x)
    elif x < l and y < l:
        z(n - 1, y, x)

z(N, r, c)
print(result)