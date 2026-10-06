# 2026 상반기 오전 1번 문제

from collections import deque

N, M, K = list(map(int, input().split()))
GRID = [list(map(int, input().split())) for _ in range(N)]              # 0: 이동 가능 / 1: 산호초 / -1: 화석 / 2: 거북이 
turtles = [list(map(int, input().split())) + [0] for _ in range(M)]     # (r, c, 타입) / 타입 0: 거북이 / -1: 화석 / 1: 탈출
VOLCANOES = [list(map(int, input().split())) + [0] for _ in range(K)]   # (r, c, 임계값, 현재값)

DESTINATION = (N-1, N-1)

answers = [-1 for x in range(M)]        # 최종 출력할 값. 초기값은 -1.

## 0단계. 초기 맵에 거북이 배치
for turtle in turtles:
    GRID[turtle[0]][turtle[1]] = 2

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

## 1단계. 이동
## 거북이는 ID 순으로 이동. 매 차례 최단 거리 탐색
## 장애물 : 산호초 / 다른 거북 / 화석       <=>     (화산 칸에는 진입 가능)
## 이동규칙 : 최단경로 존재시, [우-하-좌-상] 순서로 이동. 경로 없으면 가만히.

# 우 하 좌 상 (0 1 2 3)
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def bfs(start_r, start_c):
    queue = deque([(-1, start_r, start_c)])     # (초기방향, r, c) | 초기방향을 -1로 설정해 최초 1회만 방향 업데이트
    visited = [[False for _c in range(N)] for _r in range(N)]

    while queue:
        dir, r, c = queue.popleft()

        if visited[r][c]: continue
        visited[r][c] = True

        if (r, c) == DESTINATION:       # 골인 지점에 도착 가능한 것이 확인 되므로 (현재 위치 + 초기 이동 방향)을 반환
            return (start_r + dr[dir], start_c + dc[dir])

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if is_valid_coord(nr, nc):
                if not visited[nr][nc]:
                    if GRID[nr][nc] == 0:
                        if dir == -1: queue.append((i, nr, nc)) # 최초 1회에 한해 방향 저장
                        else: queue.append((dir, nr, nc))

    return (start_r, start_c)           # 도착 불가 => 그 자리에 그대로.

def step1(iteration):
    for tid, turtle in enumerate(turtles):
        if turtle[2] != 0: continue      # 죽은 거북이, 탈출 거북이 제외

        start_r, start_c = turtle[0], turtle[1]
        next_r, next_c = bfs(start_r, start_c)

        if (start_r, start_c) == (next_r, next_c): continue

        turtle[0], turtle[1] = next_r, next_c
        GRID[start_r][start_c] = 0
        GRID[next_r][next_c] = 2

        # 목적지(N-1, N-1) 도달 시
        if (next_r, next_c) == DESTINATION:
            GRID[next_r][next_c] = 0
            answers[tid] = iteration
            turtle[2] = 1

## 2단계. 화산 압력 10 증가

def step2():
    for volcanoe in VOLCANOES:
        volcanoe[3] += 10

## 3단계. 화산 분출 및 연쇄 반응
## 임계치 '이상'인 화산은 열기 분출
## 3-1 단계. 열기 전파. 
##      해당 칸에 축적된 압력만큼. 상하좌우 각 방향으로 이전 칸 대비 절반 (소수점은 버림)
##      (중요) 산호초에 막히거나, 열기가 0이 되면 전파 중단. 여러 열기가 도달 시 누적.
## 3-2 단계. 연쇄 반응.
##      아직 분출하지 않은 화산 중, (현재 압력 + 외부 누적 열기)가 임계치를 초과하면 분출.
##      (중요) 외부 열기는 조건만 만족시킬 뿐, 실제 압력 자체를 높이진 않음. (즉 분출 효과는 현재 압력 기준으로 계산)
##      새로 분출하는 화산이 없을 때까지 반복
## 3-3 단계. 화석화
##      분출 종료 후, 살아있는 거북이가 위치한 칸의 총 열기 합이 '20 이상' 이면 화석이 된다.

heat_map = [[0 for _c in range(N)] for _r in range(N)]
exploded = [False for _ in range(K)]

def explode(r, c, heat):
    # 현재 위치
    heat_map[r][c] += heat
    # 상
    for i in range(1, N):
        if not is_valid_coord(r-i, c): break
        if GRID[r-i][c] == 1: break
        heat_map[r-i][c] += heat_map[r-i+1][c] // 2
    # 하
    for i in range(1, N):
        if not is_valid_coord(r+i, c): break
        if GRID[r+i][c] == 1: break
        heat_map[r+i][c] += heat_map[r+i-1][c] // 2
    # 좌
    for i in range(1, N):
        if not is_valid_coord(r, c-i): break
        if GRID[r][c-i] == 1: break
        heat_map[r][c-i] += heat_map[r][c-i+1] // 2
    # 우
    for i in range(1, N):
        if not is_valid_coord(r, c+i): break
        if GRID[r][c+i] == 1: break
        heat_map[r][c+i] += heat_map[r][c+i-1] // 2

def step3():
    exp_queue = [(vid, r, c, threshold, pressure) for vid, (r, c, threshold, pressure) in enumerate(VOLCANOES) if pressure >= threshold]

    # 3-1, 3-2 단계
    while exp_queue:
        vid, r, c, threshold, pressure = exp_queue.pop()

        if exploded[vid]: continue
        exploded[vid] = True

        explode(r, c, threshold)

        for vid, (r, c, threshold, pressure) in enumerate(VOLCANOES):
            if exploded[vid]: continue
            if heat_map[r][c] + pressure >= threshold:
                exp_queue.append((vid, r, c, threshold, pressure))

    # 3-3 단계
    for turtle in turtles:
        if turtle[2] == 0:
            tr, tc = turtle[0], turtle[1]
            if heat_map[tr][tc] >= 20:
                turtle[2] = -1
                GRID[tr][tc] = -1

## 4단계. 분출한 모든 화산 0으로 초기화.

def step4():
    global exploded, heat_map
    for id, is_exploded in enumerate(exploded):
        if is_exploded:
            VOLCANOES[id][3] = 0
    exploded = [False for _ in range(K)]
    heat_map = [[0 for _c in range(N)] for _r in range(N)]

######################################
######################################

def is_over():
    for turtle in turtles:
        if turtle[2] == 0: return False
    return True

for iteration in range(1, 101):
    if is_over(): break
    step1(iteration)
    step2()
    step3()
    step4()

for answer in answers:
    print(answer)
