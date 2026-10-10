from collections import deque

N, T = map(int, input().split())
F = [list(input().strip()) for _ in range(N)]               # 신봉 음식
B = [list(map(int, input().split())) for _ in range(N)]     # 신앙심

# 상 하 좌 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

def print_arr(title, arr):
    print(f"# TITLE : {title}")
    for row in arr:
        print(row)
    print("#" * 60)

# 1. 아침
# 모든 학생이 신앙심 1 획득

def step1():
    for r in range(N):
        for c in range(N):
            B[r][c] += 1

# 2. 점심
# 인접학생들과 신봉 음식이 '동일'할 경우 그룹 형성
# 그룹 대표자 선정 규칙 : (1) 신앙심 큰 (2) r 작은 (3) c 작은
# 대표의 신앙심은 (그룹원수-1) 만큼 증가, 나머지 그룹원은 1씩 감소

def get_groups():
    """ 모든 그룹을 반환 """
    visited = [[False for _c in range(N)] for _r in range(N)]
    groups = []     # [[(b,r,c,f), (b,r,c,f)], [...], [...]]

    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue
            group = []                          # (b, r, c, f)
            queue = deque([(B[r][c], r, c)])    # (b, r, c)

            while queue:
                b, fr, fc = queue.popleft()
                if visited[fr][fc]: continue
                visited[fr][fc] = True
                group.append([b, fr, fc, F[r][c]])

                for i in range(4):
                    nr, nc = fr + dr[i], fc + dc[i]
                    if not is_valid_coord(nr, nc): continue
                    if F[nr][nc] != F[r][c]: continue
                    if visited[nr][nc]: continue
                    queue.append((B[nr][nc], nr, nc))

            if group:
                groups.append(group)

    return groups

def get_group_representatives(groups):
    """ 해당 그룹의 대표를 반환 (신앙심 양도 포함) """
    representatives = []                    # (b, r, c, f)
    for group in groups:
        group.sort(key=lambda x: (-x[0], x[1], x[2]))   # 그룹대표자 선정 규칙 참고 (1) 신앙심 큰 (2) r 작은 (3) c 작은
        for i, (b, r, c, f) in enumerate(group):
            if i == 0:
                B[r][c] += len(group)-1
            else:
                B[r][c] -= 1
            group[i][0] = B[r][c]
        representatives.append(group[0])
    return representatives

def step2():
    groups = get_groups()                               # [1] 그룹을 찾는다
    representatives = get_group_representatives(groups) # [2] 각 그룹의 대표자를 찾아 신앙심을 모은다
    return representatives

# 3. 저녁
# 전파는 세 그룹 순서대로 진행 : 단일 조합(T,C,M) -> 이중 조합(TC, TM, CM) -> 삼중 조합(TCM)
# 각 그룹에서의 전파 순서 : (1) 대표자 신앙심 큰 (2) 대표자 r 작은 (3) 대표자 c 작은
# 전파자(대표)는 자신의 신앙심 B 중 1만 남기고 나머지를 간절함 (x=B-1) 으로 바꿔 전파
# 전파 방향 : B % 4 => 상(0) 하(1) 좌(2) 우(3)
# 전파 방향으로 한 칸씩 이동하며 전파 시도 / 격자 나가거나, 간절함(x)가 0이 되면 전파 종료
# 전파 대상의 신봉 음식이 다른 경우에만 전파 (같은 경우 그냥 pass)
# [1] 강한 전파 : 간절함(x) > 전파대상 신앙심(y)
#   -) 동일한 음식을 신봉하게 됨
#   -) 전파자의 간절함은 (y+1)만큼 깎임 (즉 x -= y+1)
#   -) 전파 대상의 신앙심은 +1 상승 (즉 y += 1)
#   -) 전파자의 간절함이 0이 되면 종료
# [2] 약한 전파 : 간절함(x) <= 전파대상 신앙심(y)
#   -) 음식 조합을 신봉하게 됨
#   -) 전파자의 간절함은 0이 되고 전파는 종료
#   -) 전파 대상의 신앙심은 +x 상승 (즉 y += x)
# (주의) 전파를 당한 학생은 '당일'에 전파를 하지 않음. (즉 대표자였는데 전파당했을 경우를 주의해야 할 듯)

def step3(representatives):
    representatives.sort(key=lambda k: (len(k[3]), -k[0], k[1], k[2]))
    blocked_representatives = set()

    for representative in representatives:
        rep_b, rep_r, rep_c, rep_f = representative
        if (rep_r, rep_c) in blocked_representatives: continue

        B[rep_r][rep_c] = 1
        x, direction = rep_b-1, rep_b % 4

        r, c = rep_r, rep_c
        while True:
            r += dr[direction]
            c += dc[direction]
            if not is_valid_coord(r, c): break          # 격자 나가면 종료
            if x == 0: break                            # 간절함이 0이면 종료
            if F[r][c] == F[rep_r][rep_c]: continue     # 신봉대상이 같을 경우 pass

            if [B[r][c], r, c, F[r][c]] in representatives:
                blocked_representatives.add((r, c))      # 전파 당했으면 전파 불가하게

            if x > B[r][c]:                             # [1] 강한 전파
                F[r][c] = F[rep_r][rep_c]               # 동일 음식 신봉
                B[r][c] += 1                            # 전파 대상의 신앙심 1 상승
                x -= B[r][c]                            # 전파자의 간절함 (y+1)만큼 감소

            else:                                       # [2] 약한 전파
                combination = set(F[rep_r][rep_c]) | set(F[r][c])
                F[r][c] = "".join(sorted(combination))  # 음식 조합을 신봉하게 됨
                B[r][c] += x                            # 전파 대상의 신앙심 x 상승
                x = 0                                   # 전파자의 간절함 0

    beliefs_acc = {
        'CMT': 0,   # 민트초코우유
        'CT': 0,    # 민트초코
        'MT': 0,    # 민트우유
        'CM': 0,    # 초코우유
        'M': 0,     # 우유
        'C': 0,     # 초코
        'T': 0,     # 민트
    }

    for r in range(N):
        for c in range(N):
            beliefs_acc[F[r][c]] += B[r][c]

    print(" ".join(map(str, beliefs_acc.values())))

###########################################################################

for t in range(T):
    step1()
    reps = step2()
    step3(reps)