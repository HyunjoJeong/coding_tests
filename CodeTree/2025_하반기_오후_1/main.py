from collections import deque

N, K, L = map(int, input().split())                             # 2 <= N <= 30 | 1 <= K <= 50 | 1 <= L <= 50
GRID = [list(map(int, input().split())) for _ in range(N)]      # 먼지 정보가 적혀 있음. -1은 벽
GRID_robots = [[False for _c in range(N)] for _r in range(N)]   # 로봇 유무를 저장
robots = [list(map(int, input().split())) for _ in range(K)]    # (r, c) 저장
for robot in robots:
    robot[0], robot[1] = robot[0]-1, robot[1]-1
    GRID_robots[robot[0]][robot[1]] = True


# 좌 상 우 하
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

def print_arr(title, arr):
    print(title)
    for row in arr:
        print(row)
    print("=" * 50)

# 1. 청소기 이동
# 각 로봇 청소기는 '이동거리'가 가장 가까운 오염 격자로 이동
# 가까운 격자가 여러 개일 경우 : (1) 행 작은 순 (2) 열 작은 순
# (주의) 벽 or 다른 로봇 청소기 격자는 통과 불가

# 전략: BFS

def find_closest_dust(start_r, start_c):
    """ 이동할 수 있는 가장 가까운 먼지 격자를 반환. 없으면 현재 격자 반환 """
    min_dist = float('inf')
    nearby_dusts = []                       # (dist, r, c)
    visited = [[False for _c in range(N)] for _r in range(N)]
    queue = deque([(0, start_r, start_c)])  # (dist, r, c)

    while queue:
        dist, r, c = queue.popleft()

        if dist > min_dist:
            break
        if visited[r][c]:
            continue
        if GRID[r][c] > 0:
            min_dist = dist
            nearby_dusts.append((dist, r, c))

        visited[r][c] = True

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not is_valid_coord(nr, nc): continue
            if GRID_robots[nr][nc]: continue            # 다른 로봇
            if GRID[nr][nc] < 0: continue               # 벽
            if visited[nr][nc]: continue
            queue.append((dist+1, nr, nc))

    if nearby_dusts:
        nearby_dusts.sort()
        next_r, next_c = nearby_dusts[0][1], nearby_dusts[0][2]
        return next_r, next_c
    else:
        return start_r, start_c

def move_robot(rid, start_r, start_c, next_r, next_c):
    if (start_r, start_c) == (next_r, next_c):
        return

    GRID_robots[start_r][start_c] = False
    GRID_robots[next_r][next_c] = True
    robots[rid] = [next_r, next_c]

def step1():
    for rid, (start_r, start_c) in enumerate(robots):
        next_r, next_c = find_closest_dust(start_r, start_c)
        move_robot(rid, start_r, start_c, next_r, next_c)

# 2. 청소
# 청소기는 [현재 위치 + 전방 + 좌측 + 우측] 4개 격자를 청소할 수 있음
# 4가지 방향 중 가장 청소할 수 있는 먼지가 많은 방향을 청소
# 합이 같은 방향이 여럿일 경우 : (1) 우 (2) 하 (3) 좌 (4) 상 순서로 선택
# 각 격자마다 최대 청소할 수 있는 먼지는 20
# 각 청소기마다 순서대로 진행됨

SWEEP = 20

def find_min_direction(r, c):
    queue = []  # (먼지양, 방향)

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not is_valid_coord(nr, nc): return i # 해당 위치가 범위 밖일 경우
        if GRID[nr][nc] < 0: return i           # 해당 위치가 벽일 경우
        queue.append((min(20, GRID[nr][nc]), i))

    return min(queue)[1]                        # 방향은 좌(0) 상(1) 우(2) 하(3) 이므로, 가장 작은 방향이 반환됨

def clean(r, c, min_dir):
    GRID[r][c] = max(GRID[r][c] - SWEEP, 0)
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not is_valid_coord(nr, nc): continue
        if GRID[nr][nc] < 0: continue
        if i == min_dir: continue
        GRID[nr][nc] = max(GRID[nr][nc] - SWEEP, 0)

def step2():
    for r, c in robots:
        min_dir = find_min_direction(r, c)
        clean(r, c, min_dir)

# 3. 먼지 축적
# 먼지가 있는 모든 격자칸에 먼지가 5씩 추가

def step3():
    for r in range(N):
        for c in range(N):
            if GRID[r][c] > 0:
                GRID[r][c] += 5

# 4. 먼지 확산
# 깨끗한 격자에 주변 4방향 격자의 먼지량 합을 10으로 나눈 값만큼 먼지가 확산 (소수점 버림)
# 모든 깨끗한 격자에 대해 '동시'에 진행

def get_next_dust(r, c):
    total = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not is_valid_coord(nr, nc): continue
        if GRID[nr][nc] < 0: continue
        total += GRID[nr][nc]
    return total // 10

def step4():
    queue = []          # (r, c, next_dust)
    for r in range(N):
        for c in range(N):
            if GRID[r][c] == 0:
                queue.append((r, c, get_next_dust(r, c)))
    for r, c, next_dust in queue:
        GRID[r][c] = next_dust

# 5. 출력
# 총 먼지량을 출력

def step5():
    total = 0
    for r in range(N):
        for c in range(N):
            if GRID[r][c] > 0:
                total += GRID[r][c]
    print(total)
    return total

##########################################################################################

for l in range(L):
    step1()
    step2()
    step3()
    step4()
    if step5() == 0:
        break