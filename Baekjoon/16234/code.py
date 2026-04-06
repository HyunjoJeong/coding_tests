## 16234. 인구이동
## https://www.acmicpc.net/problem/16234
## 전략: BFS로 연합국 찾기

from collections import deque

N, L, R = map(int, input().strip().split())
A = [list(map(int, input().strip().split())) for _ in range(N)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

days = 0

while True:
    unionCount = 0
    visited =[[False for _c in range(N)] for _r in range(N)]

    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            visited[r][c] = True
            
            populations = A[r][c]
            union = [(r, c)]
            searchList = deque([(r, c)])

            while searchList:
                sr, sc = searchList.popleft()
                for i in range(4):
                    nr, nc = sr + dr[i], sc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and (L <= abs(A[nr][nc] - A[sr][sc]) <= R):
                        populations += A[nr][nc]
                        visited[nr][nc] = True
                        union.append((nr, nc))
                        searchList.append((nr, nc))
            
            unionSize = len(union)
            if unionSize > 1:
                unionCount += 1
                for (cr, cc) in union:
                    A[cr][cc] = populations // unionSize

    if unionCount == 0: break
    days += 1

print(days)