## 1938. 통나무 옮기기
## https://www.acmicpc.net/problem/1938
## 전략: BFS + B의 중심정만 이동하고, visited를 3차원 [r][c][수직/수평] 으로 관리하여 돌릴 수 있는지를 체킹.
from collections import deque

N = int(input().strip())
matrix = [[x for x in input().strip()] for _ in range(N)]

# B, E의 중심점과 수직/수평 여부를 반환 => (r, c, d) (참고, d는 수직: 1, 수평: 0)
def getInfo(target: str):
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == target:
                isParallel = c+1 < N and matrix[r][c+1] == target
                return (r, c+1, 0) if isParallel else (r+1, c, 1)

def canMove(r: int, c: int, d: int):
    if d:       # 수직 형태
        if not (0 < r < N-1 and 0 <= c < N): return False
        if matrix[r-1][c] == '1' or matrix[r][c] == '1' or matrix[r+1][c] == '1': return False
    else:       # 수평 형태
        if not (0 <= r < N and 0 < c < N-1): return False
        if matrix[r][c-1] == '1' or matrix[r][c] == '1' or matrix[r][c+1] == '1': return False
    return True

def canRotate(r: int, c: int):
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if not (0 <= i < N and 0 <= j < N): return False
            if matrix[i][j] == '1': return False
    return True

def bfs():
    Br, Bc, Bd = getInfo('B')
    Er, Ec, Ed = getInfo('E')

    visited = [[[False for _d in range(2)] for _c in range(N)] for _r in range(N)]
    visited[Br][Bc][Bd] = True
    queue = deque([(Br, Bc, Bd, 0)])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        r, c, d, actionCount = queue.popleft()

        if r == Er and c == Ec and d == Ed:
            return actionCount

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if canMove(nr, nc, d) and not visited[nr][nc][d]:
                visited[nr][nc][d] = True
                queue.append((nr, nc, d, actionCount + 1))
        
        nd = 1-d
        if canRotate(r, c) and not visited[r][c][nd]:
            visited[r][c][nd] = True
            queue.append((r, c, nd, actionCount + 1))

    return 0

print(bfs())