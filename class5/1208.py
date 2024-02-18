import sys
from itertools import combinations
N, S = map(int, input().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
arr1, arr2 = arr[:N//2], arr[N//2:]

def sub(arr):
    cnt = [0]
    for i in range(1, len(arr) + 1):
        for c in combinations(arr, i):
            cnt.append(sum(c))
    cnt.sort()
    return cnt

def lower_bound(start, end, k):
    while(start < end):
        mid = (start + end) // 2
        if vec2[mid] < k:
            start = mid + 1
        elif vec2[mid] >= k:
            end = mid

    return end

    
def upper_bound(start, end, k):
    while(start < end):
        mid = (start + end) // 2
        if vec2[mid] <= k:
            start = mid + 1
        elif vec2[mid] > k:
            end = mid

    return end

res = 0
vec1 = sub(arr1)
vec2 = sub(arr2)
for i in range(len(vec1)):
    num = S - vec1[i]
    res += upper_bound(0, len(vec2), num) - lower_bound(0, len(vec2), num)
if S == 0:
    res -= 1
print(res)