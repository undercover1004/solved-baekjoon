N = int(input())

arr = [[' ' for _ in range(2 * N)] for _ in range(N)]

def star(a, b, size):
    if size == 3:
        arr[a][b] = '*'
        arr[a + 1][b - 1] = '*'
        arr[a + 1][b + 1] = '*'
        for i in range(b - 2, b + 3):
            arr[a + 2][i] = '*'
    else:
        size = size // 2
        star(a, b, size)
        star(a + size, b - size, size)
        star(a + size , b + size, size)

star(0, N - 1, N)
for s in arr:
    print("".join(s))