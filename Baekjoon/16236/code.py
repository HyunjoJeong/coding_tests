## 16236. 아기상어
## https://www.acmicpc.net/problem/16236
## 전략: BFS

from collections import deque
import heapq

N = int(input().strip())
matrix = [list(map(int, input().strip().split())) for _ in range(N)]

elapsedTime = 0
sharkSize = upgradeCount = 2

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 초기 상어 위치
def findStartIndex():
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 9:
                return (r, c)

# 먹이 탐색: (1) 가장 가까운 (2) 가장 row가 작은 (3) 가장 col이 작은
def bfs(startR: int, startC: int):
    visited = [[False for _c in range(N)] for _r in range(N)]
    visited[startR][startC] = True

    path = deque([(0, startR, startC)])     # (거리, r, c)
    destinations = []                       # (거리, r, c) / 먹을 수 있으면 저장해두기.

    while path:
        d, r, c = path.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and matrix[nr][nc] <= sharkSize:
                visited[nr][nc] = True
                path.append((d+1, nr, nc))
                
                if 0 < matrix[nr][nc] < sharkSize:
                    heapq.heappush(destinations, (d+1, nr, nc))

    return destinations[0] if destinations else (None, None, None)

# 이동 및 포식
def moveAndEat(distance: int, startR: int, startC: int, nextR: int, nextC: int):
    global elapsedTime, upgradeCount, sharkSize

    elapsedTime += distance
    matrix[startR][startC] = 0
    matrix[nextR][nextC] = 9

    upgradeCount -= 1
    if upgradeCount == 0:
        sharkSize += 1
        upgradeCount = sharkSize

while True:
    startR, startC = findStartIndex()
    distance, nextR, nextC = bfs(startR, startC)
    if not distance: break
    moveAndEat(distance, startR, startC, nextR, nextC)

print(elapsedTime)