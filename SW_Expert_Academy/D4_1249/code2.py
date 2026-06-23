
import heapq

T = int(input())
output_buffer = []

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

INF = float('inf')

for t in range(T):
    S = int(input())
    grid = [list(map(int, input())) for _ in range(S)]

    min_costs = [[INF for _c in range(S)] for _r in range(S)]
    min_costs[0][0] = 0
    min_queue = [(0, 0, 0)] # (cost, r, c)

    while min_queue:
        cost, r, c = heapq.heappop(min_queue)

        if (r, c) == (S - 1, S - 1):
            output_buffer.append(cost)
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < S and 0 <= nc < S:
                new_cost = cost + grid[nr][nc]
                if new_cost < min_costs[nr][nc]:
                    min_costs[nr][nc] = new_cost
                    heapq.heappush(min_queue, (cost + grid[nr][nc], nr, nc))

for t in range(T):
    print(f"#{t+1} {output_buffer[t]}")