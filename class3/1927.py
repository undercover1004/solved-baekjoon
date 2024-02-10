from queue import PriorityQueue
import sys

queue = PriorityQueue()
result = []

N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if queue.empty():
            result.append(0)
        else:
            result.append(queue.get())
    else:
        queue.put(num)

for num in result:
    print(num)
