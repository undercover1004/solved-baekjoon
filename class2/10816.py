N = int(input())
card = list(map(int, input().split()))
card.sort()
M = int(input())
vec = list(map(int, input().split()))

def lower_bound(k):
    start = 0
    end = N
    while(start < end):
        mid = (start + end) // 2
        if card[mid] < k:
            start = mid + 1
        elif card[mid] >= k:
            end = mid

    return end

    
def upper_bound(k):
    start = 0
    end = N
    while(start < end):
        mid = (start + end) // 2
        if card[mid] <= k:
            start = mid + 1
        elif card[mid] > k:
            end = mid

    return end


for v in vec:
    print(upper_bound(v) - lower_bound(v), end = " ")