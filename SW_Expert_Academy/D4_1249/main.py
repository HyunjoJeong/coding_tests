## 1249. 보급로
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD
## 다익스트라

import heapq

T = int(input())
answers = []

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    N = int(input())
    matrix = [input() for _ in range(N)]

    shortest_path = [[float('inf') for _c in range(N)] for _r in range(N)]
    shortest_path[0][0] = 0
    queue = [(0,0,0)]

    while queue:
        path, r, c = heapq.heappop(queue)

        if (r, c) == (N-1, N-1):
            answers.append(path)
            break

        if path > shortest_path[r][c]:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: continue

            new_path = path + int(matrix[nr][nc])
            if new_path < shortest_path[nr][nc]:
                shortest_path[nr][nc] = new_path
                heapq.heappush(queue, (new_path, nr, nc))

for t in range(T):
    print(f"#{t+1} {answers[t]}")