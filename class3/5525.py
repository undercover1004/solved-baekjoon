N = int(input())
M = int(input())
S = input()

count = 0
result = 0
i = 0
while(i < M):
    if S[i:i+3] == 'IOI':
        count += 1
        i += 2
        if count == N:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0

print(result)