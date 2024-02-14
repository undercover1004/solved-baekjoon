import sys

TC = int(input())
INF = int(1e9)


def bf(start):

    distance[start] = 0
    for i in range(N):
        for j in range(2 * M + W):
            cur_node = graph[j][0]
            next_node = graph[j][1]
            edge_cost = graph[j][2]
            if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
                distance[next_node] = distance[cur_node] + edge_cost
                if i == N - 1:
                    return True
    return False


for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())
    distance = [10001] * (N + 1)
    graph = []
    for _ in range(M):
        a, b, c = map(int, sys.stdin.readline().split())
        graph.append((a, b, c))
        graph.append((b, a, c))

    for _ in range(W):
        a, b, c = map(int, sys.stdin.readline().split())
        graph.append((a, b, -c))

    
    if bf(1):
        print("YES")
    else:
        print("NO")

