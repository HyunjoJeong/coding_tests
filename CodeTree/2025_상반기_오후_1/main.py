from collections import deque

## N은 GRID 사이즈, Q는 실험 횟수를 의미한다.
## 아래 3단계를 Q번 만큼 반복한다.
N, Q = map(int, input().split())
GRID = [[None for _c in range(N)] for _r in range(N)] # 각 미생물이 들어올 경우 id를 숫자로 기입.

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(n, c):
    return 0 <= n < N and 0 <= c < N

def print_array(title, arr):
    print(title)
    for row in arr:
        print(row)
    print("#" * 40)

# 1. 미생물 투입
# 좌측하단(r1, c1) 우측상단(r2, c2)인 직사각형 영역에 미생물 투입. 해당 영역에 다른 미생물 있을 시 덮어쓰기 (완전히 덮는 경우 체크 필요)
# 기존 미생물 무리가 영역이 나눠질 경우 -> 해당 미생물 전부 제거 (여러번에 나뉘어 사라지는 경우 체크 필요)

# 각 미생물 별 실제 점유 토지 / key: 미생물ID, value: (r,c) 배열 / len으로 토지 크기 바로 얻을 수 있음.
territories = dict({ i: [] for i in range(Q) })

def insert_micro(mid, r1, c1, r2, c2):
    """ GRID, territories에 신규 미생물 등록. 침범한 영역을 반환 """
    invaded_mids = set()

    for r in range(r1, r2):
        for c in range(c1, c2):
            if GRID[r][c] is not None:
                prev_mid = GRID[r][c]
                territories[prev_mid].remove((r, c))
                invaded_mids.add(prev_mid)
            GRID[r][c] = mid
            territories[mid].append((r, c))

    return invaded_mids

def remove_micro(mid):
    """ 해당 미생물을 GRID와 territories에서 제거 """
    territory = territories[mid]
    for r, c in territory:
        GRID[r][c] = None
    territories[mid].clear()

def check_division(mid):
    visited = [[False for _c in range(N)] for _r in range(N)]
    visit_count = 0

    territory = territories[mid]

    if not territory:   # 완전히 덮혀서 territory가 없는 경우
        return False

    queue = deque([territory[0]])

    while queue:
        r, c = queue.popleft()

        if visited[r][c]:
            continue

        visited[r][c] = True
        visit_count += 1

        if visit_count == len(territory):
            return False

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not is_valid_coord(nr, nc):
                continue
            if visited[nr][nc]:
                continue
            if GRID[nr][nc] == mid:
                queue.append((nr, nc))

    return True

def step1(mid, r1, c1, r2, c2):
    invaded_mids = insert_micro(mid, r1, c1, r2, c2)
    for mid in invaded_mids:
        if check_division(mid):
            remove_micro(mid)

# 2. 배양 용기 이동
# 새로운 배양 용기로 이동하는데, 기존에 있던 미생물을 '전부' 옮겨야 함.
# (1) 가장 차지 영역이 넓은 미생물부터 옮김. 넓이가 같으면 먼저 들어온 미생물부터
# (2) 형태는 기존과 동일하게 유지. 다른 미생물과 영역 겹침 X
# (3) 옮기는 위치는 [r 작은 순 -> c 작은 순]
# (4) 옮길 수 없는 미생물 무리는 제거

def clear_grid():
    for r in range(N):
        for c in range(N):
            GRID[r][c] = None

def step2():
    clear_grid()
    sorted_molecules = sorted([(-len(territory), mid) for mid, territory in territories.items() if territory])

    for molecule in sorted_molecules:
        mid = molecule[1]
        territory = territories[mid]
        min_r = min(territory, key=lambda x: x[0])[0]
        min_c = min(territory, key=lambda x: x[1])[1]

        i = 0
        is_fit = True
        start_r, start_c = 0, 0

        while i < N * N:
            r = i // N
            c = i % N
            i += 1
            is_fit = True

            for tr, tc in territory:
                sr, sc = r + (tr - min_r), c + (tc - min_c)
                if not is_valid_coord(sr, sc):
                    is_fit = False
                    break
                if GRID[sr][sc] is not None:
                    is_fit = False
                    break

            if is_fit:
                start_r, start_c = r, c
                break

        if is_fit:
            next_territory = []

            for tr, tc in territory:
                sr, sc = start_r + (tr - min_r), start_c + (tc - min_c)
                GRID[sr][sc] = mid
                next_territory.append((sr, sc))

            territories[mid] = next_territory
        else:
            territories[mid].clear()

# 3. 결과 기록
# "인접한 무리" : 상하좌우로 맞닿은 면이 있는 두 무리
# 모든 인접한 무리 쌍에 대해, 각 쌍의 영역의 곱을 합한다.
# e.g) A,B가 인접 & B,C가 인접 -> (A넓이 * B넓이) + (B넓이 * C넓이)
# (참고) 따라서 인접한 무리가 없으면 답은 0

def step3():
    total = 0
    related_mids = set()

    for r in range(N):
        for c in range(N):
            if r < N-1:
                if GRID[r][c] is not None and GRID[r+1][c] is not None:
                    if GRID[r][c] != GRID[r+1][c]:
                        related_mids.add(tuple(sorted([GRID[r][c], GRID[r+1][c]])))
            if c < N-1:
                if GRID[r][c] is not None and GRID[r][c+1] is not None:
                    if GRID[r][c] != GRID[r][c+1]:
                        related_mids.add(tuple(sorted([GRID[r][c], GRID[r][c+1]])))

    for (mid1, mid2) in related_mids:
        total += len(territories[mid1]) * len(territories[mid2])

    print(total)

for q in range(Q):
    _r1, _c1, _r2, _c2 = map(int, input().split())
    step1(q, _r1, _c1, _r2, _c2)
    step2()
    step3()
