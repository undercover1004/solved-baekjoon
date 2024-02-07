N, M = map(int,input().split())
lan = []
for _ in range(N):
    lan.append(int(input()))

start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2
    sum  = 0
    for num in lan:
        sum += num // mid
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
