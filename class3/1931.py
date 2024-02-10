N = int(input())
time = []
for _ in range(N):
    a, b = map(int, input().split())
    time.append((a, b))

time.sort(key = lambda x:(x[1], x[0]))

result = 0
end = 0
for i in range(N):
    if end <= time[i][0]:
        result += 1
        end = time[i][1]

print(result)