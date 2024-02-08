N = int(input())
num = list(map(int, input().split()))
num.sort()
M = int(input())
A = list(map(int, input().split()))

def find(k):
    start = 0
    end = len(num) - 1
    while(start <= end):
        mid = (start + end) // 2
        if num[mid] < k:
            start = mid + 1
        elif num[mid] > k:
            end = mid - 1
        elif num[mid] == k:
            return True
    return False

for k in A:
    if find(k):
        print("1")
    else:
        print("0")
    