N = int(input())

paper = [list(map(int, input().split())) for _ in range(N)]

blue = 0
white = 0

def sum(n, x, y):
    result = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            result += paper[i][j]
    return result


def devide(n, x, y):
    global white
    global blue
    if sum(n, x, y) == n * n:
        blue += 1
        return
    elif sum(n, x, y) == 0:
        white += 1
        return
    else:
        devide(n // 2, x, y)
        devide(n //2, x + n // 2, y)
        devide(n // 2, x , y + n // 2)
        devide(n // 2, x + n // 2, y + n // 2)

devide(N, 0, 0)
print(white)
print(blue)