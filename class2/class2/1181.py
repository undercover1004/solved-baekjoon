N = int(input())

words = []
for _ in range(N):
    word = str(input())
    if word in words:
        continue
    words.append(word)

words.sort()
words.sort(key=len)
for w in words:
    print(w)