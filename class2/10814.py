N = int(input())

online = []
for i in range(N):
    age, name = input().split()
    age = int(age)
    online.append((age, name, i))

online.sort(key = lambda x:(x[0], x[2]))

for a, b, c in online:
    print(a, b)