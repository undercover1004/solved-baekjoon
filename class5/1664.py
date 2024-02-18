N = int(input())

def odd(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

prime = []
for i in range(2, N + 1):
    if odd(i):
        prime.append(i)

print(prime)
res = 0
start, end = 0, 0
while end <= len(prime):
    if sum(prime[start:end]) == N:
        end += 1
        res += 1
    elif sum(prime[start:end]) < N:
        end += 1
    else:
        start += 1

print(res)