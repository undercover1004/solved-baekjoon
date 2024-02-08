N = int(input())

def odd(n):
    if n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1 ):
        if n % i == 0:
            return False
    return True

result = 0
num = list(map(int, input().split()))
for n in num:
    if odd(n):
        result += 1
print(result)