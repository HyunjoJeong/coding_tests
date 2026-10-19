# https://www.codetree.ai/ko/frequent-problems/hsat/problems/optimizing-battery-efficiency/description
# N x M 이 16이하니까, 최대로 해봤자 4x4 or 3x5 or 2x8 정도이다. (1x10 까지는 가능)
# 그러면 그냥 다 조사하자.

N, M = map(int, input().split())
GRID = [list(map(int, input().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

components = set()

def dfs(cell_list):
    if len(cell_list) == 5:
        components.add(frozenset(cell_list))
        return

    neighbors = set()
    for r, c in cell_list:
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if (nr, nc) not in cell_list:
                    neighbors.add((nr, nc))

    for neighbor in neighbors:
        dfs(cell_list + [neighbor])

for r in range(N):
    for c in range(M):
        dfs([(r, c)])

comp_list = list(components)
comp_len = len(comp_list)
max_score = -float('inf')

for i in range(comp_len):
    for j in range(i+1, comp_len):
        A, B = comp_list[i], comp_list[j]
        if len(A & B) == 2:
            sumA = sum(GRID[r][c] for r, c in A)
            sumB = sum(GRID[r][c] for r, c in B)
            total = sumA + sumB
            if total > max_score:
                max_score = total

print(max_score)