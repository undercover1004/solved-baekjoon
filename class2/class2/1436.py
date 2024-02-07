N = int(input())

def check(n):
    n = str(n)
    for i in range(len(n)):
        if n[i:i+3] == '666':
            return True

    return False

k = 0
num = 666
while(True):
    if check(num):
        k += 1
    if k == N:
        print(num)
        break
    num += 1

