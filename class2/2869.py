A, B, V = map(int, input().split())

height = 0
if (V - A) % (A - B) == 0:
    days = (V - A) // (A - B) + 1
else:
    days = (V - A) // (A - B) + 2
print(days)