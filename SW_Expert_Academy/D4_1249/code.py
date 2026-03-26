## 1249. 보급로
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15QRX6APsCFAYD

## 전략: 다익스트라
import heapq

N = int(input())
outputBuffer = []

def solve():
    INF = float('inf')
    minCosts = [[INF] * SIZE for _ in range(SIZE)]
    minCosts[0][0] = 0

    # 우선순위 큐 (row, col, cost) / dr, dc: 상하좌우 이동용 방향벡터
    pq = [(0, 0, 0)]
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while pq:
        r, c, cost = heapq.heappop(pq)

        if r == SIZE - 1 and c == SIZE - 1:
            outputBuffer.append(cost)
            break

        if cost > minCosts[r][c]:
            continue

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < SIZE and 0 <= nc < SIZE:
                newCost = cost + grid[nr][nc]

                if newCost < minCosts[nr][nc]:
                    minCosts[nr][nc] = newCost
                    heapq.heappush(pq, (nr, nc, newCost))

## 입력
for n in range(N):
    SIZE = int(input())
    grid = [list(map(int, input())) for _ in range(SIZE)]

    solve()

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")