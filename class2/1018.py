N, M = map(int, input().split())
board = [list(map(str, input())) for _ in range(N)]

result = 64
def change(n, m):
    global result
    # 왼쪽 위가 검정
    sum1 = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            if (i + j) % 2 == 0:
                if board[i][j] == 'B':
                    sum1 += 1
            else:
                if board[i][j] == 'W':
                    sum1 += 1
     
    sum2 = 0
    for i in range(n, n+8):
        for j in range(m, m+8):
            if (i + j) % 2 == 0:
                if board[i][j] == 'W':
                    sum2 += 1
            else:
                if board[i][j] == 'B':
                    sum2 += 1
    result = min(result, sum1, sum2)

def find():
    x = N - 8
    y = M - 8
 
    for i in range(x + 1):
        for j in range(y + 1):
            change(i, j)

find()
print(result)

