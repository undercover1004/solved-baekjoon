import heapq
import sys

T = int(input())

for _ in range(T):
    visited = [0]* 1000001
    maxheap = []
    minheap = []
    N = int(input())
    for i in range(N):
        a, k = sys.stdin.readline().rstrip().split()
        if a == 'I':
            heapq.heappush(minheap, (int(k), i))
            heapq.heappush(maxheap, (-int(k), i))
            visited[i] = 1
        else:
            if int(k) == 1:
                while maxheap and visited[maxheap[0][1]] == 0:
                        heapq.heappop(maxheap)
                if maxheap:
                    visited[maxheap[0][1]] = 0
                    heapq.heappop(maxheap)
                    # 최대값 배열에서 최소값 삭제
                    # 삭제한 인덱스 기억
            else:
                while minheap and visited[minheap[0][1]] == 0:
                        heapq.heappop(minheap)
                if minheap: 
                    visited[minheap[0][1]] = 0
                    heapq.heappop(minheap)
                    # 최소값 배열에서 최소값 삭제
                    # 삭제한 인덱스 기억

    # 겹치는 부분만 남기기(찌꺼기 제거)
    while maxheap and visited[maxheap[0][1]] == 0:
        heapq.heappop(maxheap)
    while minheap and visited[minheap[0][1]] == 0:
        heapq.heappop(minheap)

    if minheap == []:
        print("EMPTY")
    else:
        print(- maxheap[0][0], minheap[0][0])
