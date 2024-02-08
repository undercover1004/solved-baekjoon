N = int(input())

result = []
for i in range(1, N + 1):
    sum = i
    d = 1
    while(True):
        if i // d == 0:
            break
        sum += (i % (d * 10)) // d
        d *= 10
    if sum == N:
        result.append(i)

if not result:
    print("0")
else:
    print(result[0])
