N = int(input())

line = 1
cnt = 1

while(cnt < N):
    cnt += 6 * line
    line += 1

if N == 1:
    print("1")
else:
    print(line)