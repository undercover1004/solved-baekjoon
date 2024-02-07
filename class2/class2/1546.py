N = int(input())
score = list(map(int, input().split()))
M = max(score)

sum = 0
for num in score:
    sum += num
result = sum * 100 / (len(score) * M)
print(result)