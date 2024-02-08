N = int(input())
num = []
sum = 0
for _ in range(N):
    n = int(input())
    num.append(n)
    sum += n
               
num.sort()
print(round(sum / len(num)))
print(num[N // 2])
k = num[0]
num_tuple = []
cnt = 0
for i in range(0, len(num)):
    if num[i] == k:
        cnt += 1
    else:
        num_tuple.append((k, cnt))
        cnt = 1
        k = num[i]
num_tuple.append((k, cnt))

num_tuple.sort(key = lambda x :(-x[1], x[0]))
if len(num_tuple) == 1:
    print(num_tuple[0][0])
else:
    if num_tuple[0][1] == num_tuple[1][1]:
        print(num_tuple[1][0])
    else:
        print(num_tuple[0][0])

print(max(num) - min(num))