N, M = map(int, input().split())

namu = list(map(int, input().split()))
start = 1
end = max(namu)

def length(mid):
    sum = 0
    for n in namu:
        if n > mid:
            sum += n - mid
    return sum

while(start <= end):
    mid = (start + end) // 2
    if length(mid) >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)
