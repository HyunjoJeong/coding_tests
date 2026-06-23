
import heapq

T = int(input())
output_buffer = []

for t in range(T):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    LL = [[0 for _c in range(N)] for _r in range(N)]
    
    for r in range(N):
        for c in range(r + 1, N):
            LL[r][c] = LL[c][r] = (X[r] - X[c]) ** 2 + (Y[r] - Y[c]) ** 2
    
    visited = [False for _ in range(N)]
    min_queue = [(0, 0)] # (L^2, node)
    
    connections_count = -1
    L_squared_sum = 0

    while min_queue:
        L_squared, node = heapq.heappop(min_queue)

        if visited[node]:
            continue

        visited[node] = True
        connections_count += 1
        L_squared_sum += L_squared

        if connections_count == N - 1:
            break

        for next_node in range(N):
            if visited[next_node]: continue
            heapq.heappush(min_queue, (LL[node][next_node], next_node))

    output_buffer.append(round(E * L_squared_sum))

for t in range(T):
    print(f"#{t+1} {output_buffer[t]}")