## 19238. 스타트 택시
## https://www.acmicpc.net/problem/19238
## 전략: BFS
from collections import deque
import heapq

N, M, fuel = map(int, input().strip().split())
matrix = [input().strip().split() for _ in range(N)]
taxiR, taxiC = map(lambda x: int(x)-1, input().strip().split())

for m in range(M):
    startR, startC, endR, endC = map(lambda x: int(x)-1, input().strip().split())
    matrix[startR][startC] = f"s_{endR}_{endC}"

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def nextPassenger():
    if matrix[taxiR][taxiC][0] == 's': return (0, taxiR, taxiC)

    visited = [[False for _c in range(N)] for _r in range(N)]
    visited[taxiR][taxiC] = True
    queue = deque([(0, taxiR, taxiC)])      # (distance, r, c)
    passengers = []                         # (distance, r, c)

    while queue:
        d, r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc] or matrix[nr][nc] == '1': continue

            visited[nr][nc] = True
            queue.append((d+1, nr, nc))
            if matrix[nr][nc][0] == 's':
                heapq.heappush(passengers, (d+1, nr, nc))

    return passengers[0] if passengers else (None, None, None)

def nextDestination(endR: int, endC: int):
    visited = [[False for _c in range(N)] for _r in range(N)]
    visited[taxiR][taxiC] = True
    queue = deque([(0, taxiR, taxiC)])

    while queue:
        d, r, c = queue.popleft()
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if visited[nr][nc] or matrix[nr][nc] == '1': continue

            if nr == endR and nc == endC: 
                return (d+1, nr, nc)

            visited[nr][nc] = True
            queue.append((d+1, nr, nc))

    return (None, None, None)

def moveTo(distance: int, r: int, c: int, refill = False):
    global taxiR, taxiC, fuel

    if distance == None or distance > fuel: return False
    if refill: fuel += distance
    else: fuel -= distance

    matrix[taxiR][taxiC] = '0'
    taxiR, taxiC = r, c

    return True

def work():
    global fuel

    for i in range(M):
        pd, pr, pc = nextPassenger()
        if pd == None: return -1
        dr, dc = map(int, matrix[pr][pc].split("_")[1:])
        if not moveTo(pd, pr, pc): return -1
        if not moveTo(*nextDestination(dr, dc), True): return -1
    return fuel

print(work())