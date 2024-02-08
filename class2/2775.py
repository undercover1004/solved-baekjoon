T = int(input())

apt = [[0 for _ in range(15)] for _ in range(15)]

for i in range(1, 15):
    apt[0][i] = i

for i in range(1, 15):
    for j in range(1, 15):
        for k in range(1, j + 1):
            apt[i][j] += apt[i - 1][k]


for _ in range(T):
    a = int(input())
    b = int(input())
    print(apt[a][b])