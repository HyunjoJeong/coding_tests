# https://www.codetree.ai/ko/frequent-problems/hsat/problems/easy-workshop/description

# 조건
# 1. 시작 위치는 상관X
# 2. 상하좌우로 이동 가능 / 이동할 때마다 높아져야 한다.
# 3. 등산로의 길이는 K (K는 min(NxN, 100))
# 목표
# 가장 편안한 등산로 (인접한 높이차의 최댓값이 최소인 등산로)
# 전략
# DP, [r][c][k]에 현재위치까지 K개만큼 연결되었을 때 높이차의 최대값을 저장

N, K = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

min_map = [[[float('inf') for k in range(K+1)] for _c in range(N)] for _r in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

for r in range(N):
    for c in range(N):
        for i in range(4):
            pr, pc = r + dr[i], c + dc[i]
            if not is_valid_coord(pr, pc): continue
            diff = grid[r][c] - grid[pr][pc]
            if diff <= 0: continue
            if diff < min_map[r][c][2]:
                min_map[r][c][2] = diff

for k in range(2, K):
    for r in range(N):
        for c in range(N):
            if min_map[r][c][k] == float('inf'): continue
            for i in range(4):
                pr, pc = r + dr[i], c + dc[i]
                if not is_valid_coord(pr, pc): continue
                diff = grid[r][c] - grid[pr][pc]
                if diff <= 0: continue
                max_diff = max(diff, min_map[pr][pc][k])
                if max_diff < min_map[r][c][k+1]:
                    min_map[r][c][k+1] = max_diff

answer = float('inf')

for r in range(N):
    for c in range(N):
        if min_map[r][c][K] < answer:
            answer = min_map[r][c][K]

if answer == float('inf'):
    answer = -1

print(answer)