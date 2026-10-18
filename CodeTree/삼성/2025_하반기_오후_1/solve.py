# 2025 하반기 오후 1번 문제

import heapq
from collections import deque

# 전체 NxN
# 각 격자는 (1) 먼지 or (2) 아무것도 없거나 or (3) 물건으로 막혀있음.
# 먼지는 1~100 사이의 값.
# 각 로봇 청소기의 초기 위치에는 먼지가 없음.

# 2 <= N <= 30
# 1 <= K <= 50
# 1 <= L <= 50
# -1 <= p <= 100 (-1: 물건, 0: 빈칸, 1~100: 먼지)

N, K, L = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
robots_grid = [[False for _c in range(N)] for _r in range(N)]

robots = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(K)]
for robot in robots: robots_grid[robot[0]][robot[1]] = True

# 우-하-좌-상 의 반대인 "좌-상-우-하"
dr = [0, -1, 0, 1]
dc = [-1, 0, 1, 0]

# 1. 청소기 이동
# 가장 가까운 격자로 '순서대로' 이동 - 가까운 게 여러개면 (1) r 행번호가 작은 순 (2) c 열번호가 작은 순
# 물건이나 청소기가 있는 격자로는 이동 불가. (즉 빈칸 아니면 먼지칸만 이동 가능)

def step1():
    for ri, _robot in enumerate(robots):
        currR, currC = _robot[0], _robot[1]
        if grid[currR][currC] > 0: continue             # 현재 위치에 먼지가 남아 있을 경우 이동 없음.

        minDist = float('inf')
        candidates = []                                 # (r, c) / (1) 가장 가깝거나, (2) r 행번호가 작거나, (3) c 열번호가 작은 순
        queue = deque([(0, currR, currC)])              # (distance, r, c), 초기값은 로봇의 시작지점.

        visited = [[False for _c in range(N)] for _r in range(N)]
        visited[currR][currC] = True

        while queue:
            dist, r, c = queue.popleft()

            if dist > minDist: break                    # 제일 가까운 먼지들을 모두 찾았으면 종료
            if grid[r][c] > 0:                          # 제일 가까운 먼지칸들에만 적용됨
                minDist = dist
                heapq.heappush(candidates, (r, c))
                continue

            for i in range(4):                          # 상하좌우 탐색
                nr, nc = r + dr[i], c + dc[i]
                if not (0 <= nr < N and 0 <= nc < N): continue      # index Overflow 제외
                if visited[nr][nc] or grid[nr][nc] < 0 or robots_grid[nr][nc]: continue    # (1) 방문했거나, (2) 물건, 로봇칸은 제외

                visited[nr][nc] = True
                queue.append((dist+1, nr, nc))

        if candidates:
            nextR, nextC = candidates[0]
            robots[ri] = (nextR, nextC)
            robots_grid[currR][currC] = False
            robots_grid[nextR][nextC] = True

# 2. 청소
# 청소기가 바라보는 방향을 기준으로 [현재칸 + 좌측 + 전방 + 우측] 총 4개의 칸을 청소 가능
# 청소기가 바라보는 방향이란, 위 4개의 칸의 합이 제일 큰 방향. 즉, 가장 작은 것 제외.
# 합이 같은 경우가 여러개면 우-하-좌-상의 우선순위를 가짐. -> 청소 안 하는 칸 기준으로 좌-상-우-하
# 청소는 동시가 아니라, 청소기마다 순서대로 진행된다.

MAX_CLEANING = 20

def clean(r: int, c: int, d: int):      # 로봇의 현재 위치 r, c와 제외 방향 d
    # 현재 위치 청소
    grid[r][c] = max(grid[r][c] - MAX_CLEANING, 0)

    # 나머지 3방향 청소
    for i in range(4):
        if i == d: continue
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
            grid[nr][nc] = max(grid[nr][nc] - MAX_CLEANING, 0)

def step2():
    for (r, c) in robots:
        max_sum = 0
        except_dir = 0

        for i in range(4):
            i_sum = 0
            for j in range(4):
                if i == j: continue
                nr, nc = r + dr[j], c + dc[j]
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
                    i_sum += min(20, grid[nr][nc])
            if i_sum > max_sum:
                max_sum = i_sum
                except_dir = i

        clean(r, c, except_dir)

# 3. 먼지 축적
# '먼지가 있는' 모든 격자에 '5'씩 추가됨.

def step3():
    for _r in range(N):
        for _c in range(N):
            if grid[_r][_c] > 0: grid[_r][_c] += 5

# 4. 먼지 확산
# 깨끗한 격자 주변 4방향 격자의 먼지량 합을 10로 나눈 몫 만큼 확산.
# '동시 확산' 이므로 누적되지 않도록 주의.

def step4():
    temp = [[0 for _c in range(N)] for _r in range(N)]

    for _r in range(N):
        for _c in range(N):
            if grid[_r][_c] != 0: continue          # 물건, 먼지 칸은 제외
            nearby_dusts = 0
            for i in range(4):
                nr, nc = _r + dr[i], _c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] > 0:
                    nearby_dusts += grid[nr][nc]
            temp[_r][_c] = nearby_dusts // 10

    for _r in range(N):
        for _c in range(N):
            grid[_r][_c] += temp[_r][_c]

# 5. 출력
# 전체 공간의 총 먼지량 출력

def step5():
    dust_sum = 0
    for _r in range(N):
        for _c in range(N):
            if grid[_r][_c] > 0: dust_sum += grid[_r][_c]

    print(dust_sum)
    return dust_sum

# 위 과정을 L 번 반복.

for l in range(L):
    step1()
    step2()
    step3()
    step4()
    if step5() == 0:
        break
