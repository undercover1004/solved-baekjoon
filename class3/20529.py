import sys
from itertools import combinations

T = int(input())

def distance(a, b):
    sum = 0
    for i in range(4):
        if a[i] != b[i]:
            sum += 1
    return sum

for _ in range(T):
    N = int(sys.stdin.readline())
    mbti = list(map(str, sys.stdin.readline().split()))
    if N > 32:
        print(0)
    else:
        res = 13
        comb = combinations(mbti, 3)
        for a, b, c in comb:
            dist = 0
            dist += distance(a, b)
            dist += distance(c, b)
            dist += distance(a, c)
            res = min(res, dist)
        print(res)
                