# 2026 상반기 오후 1번 문제

from collections import deque

N, r, c, d = list(map(int, input().split()))    # N: map size, (r, c): 현재 위치, d: 현재 방향
GRID = [list(map(int, input().split())) for _ in range(N)]
r -= 1; c -= 1; d -= 1                          # 보정 (답 출력할 때는 r, c에 각각 1씩 더해줘야 함)

# 상 하 좌 우 = 0 1 2 3
DIR_ORDERS = {
    0: [0, 2, 3, 1],  # 상 좌 우 하
    1: [1, 3, 2, 0],  # 하 우 좌 상
    2: [2, 1, 0, 3],  # 좌 하 상 우
    3: [3, 0, 1, 2]   # 우 상 하 좌
}

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 남은 미방문지 수 (초기값: 전체 칸 수에서 1인 칸을 뺌)
remain_count = N * N - sum(sum(row) for row in GRID)
is_explorable = True

# 방문 여부
visited = [[False for _c in range(N)] for _r in range(N)]

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

def visit(nr, nc, dir):
    """ 방문 여부, 위치, 방향 업데이트 및 출력 """
    global remain_count, r, c, d

    remain_count -= 1
    visited[nr][nc] = True
    r, c, d = nr, nc, dir
    print(f"{nr+1} {nc+1}")

# 1. 인접 탐험 : [직진 - 좌회전 - 우회전 - 후진] 순으로 탐색 (후진은 아마 최초에만 사용될 듯)
def explore():
    global is_explorable

    for dir in DIR_ORDERS[d]:
        nr, nc = r + dr[dir], c + dc[dir]
        if is_valid_coord(nr, nc):
            if not visited[nr][nc]:
                if GRID[nr][nc] == 0:
                    visit(nr, nc, dir)
                    return

    is_explorable = False
    
# 2. 가까운 바다로 이동. (거리, r, c) 순으로 우선선택. 최단거리로 이동하되, 각 이동은 좌-하-우-상 우선순위. 도착 후 방향 유지 및 인접 탐험 재개.
# BFS 로 풀어야함
def find_nearest_sea():
    global is_explorable

    # 2-1 탐색
    search_queue = deque([(0, r, c, d)]) # (거리, r, c, d)
    searched = [[False for _c in range(N)] for _r in range(N)]

    min_dist = float('inf')
    nearest_sea_list = []

    while search_queue:
        sdist, sr, sc, sd = search_queue.popleft()

        if sdist > min_dist: break

        if searched[sr][sc]: continue
        searched[sr][sc] = True

        if sdist <= min_dist and not visited[sr][sc]:
            min_dist = sdist
            nearest_sea_list.append((sr, sc, sd))

        for dir in (2, 1, 3, 0): # 좌 하 우 상 순으로 탐색
            nsr, nsc = sr + dr[dir], sc + dc[dir]
            if is_valid_coord(nsr, nsc):
                if not searched[nsr][nsc]:
                    if GRID[nsr][nsc] == 0:
                        search_queue.append((sdist+1, nsr, nsc, dir))

    # 2-2 이동
    nearest_sea_list.sort()
    visit(*nearest_sea_list[0])
    is_explorable = True


#############################################
#############################################

visit(r, c, d) # 초기 위치도 방문 처리

while remain_count:
    if is_explorable:
        explore()
    else:
        find_nearest_sea()