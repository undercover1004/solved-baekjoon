N, K = map(int, input().split())
list = []
for _ in range(N):
    list.append(int(input()))

result = 0
sum = 0
while(list):
    num = list.pop()
    result += K // num
    K -= num * (K // num)
    if K == 0:
        break

print(result)