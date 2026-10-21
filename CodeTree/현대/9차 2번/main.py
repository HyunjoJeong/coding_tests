# https://www.codetree.ai/ko/frequent-problems/hsat/problems/mining-robot-simulation/description
# 어디선가 문제가 있는데 문제를 못 찾겠다..

from collections import deque

N, T = map(int, input().split())
GRID = [list(map(int, input().split())) for _ in range(N)]

def print_arr(arr):
    for row in arr:
        print(row)

def is_valid_coord(r, c):
    return 0 <= r < N and 0 <= c < N

best_path_from_start = [[dict() for _c in range(N)] for _r in range(N)]
best_path_from_start[0][0] = { 'value': GRID[0][0], 'prev': None } # prev2 if 좌/상 값이 동일.
for n in range(1, N):
    best_path_from_start[n][0]['value'] = best_path_from_start[n-1][0]['value'] + GRID[n][0]
    best_path_from_start[n][0]['prev'] = (n-1, 0)
    best_path_from_start[0][n]['value'] = best_path_from_start[0][n-1]['value'] + GRID[0][n]
    best_path_from_start[0][n]['prev'] = (0, n-1)
for r in range(1, N):
    for c in range(1, N):
        from_left = best_path_from_start[r][c-1]
        from_top = best_path_from_start[r-1][c]
        if from_left['value'] >= from_top['value']:
            best_path_from_start[r][c]['value'] = from_left['value'] + GRID[r][c]
            best_path_from_start[r][c]['prev'] = (r, c-1)
            if from_left['value'] == from_top['value']:
                best_path_from_start[r][c]['prev2'] = (r-1, c)
        else:
            best_path_from_start[r][c]['value'] = from_top['value'] + GRID[r][c]
            best_path_from_start[r][c]['prev'] = (r-1, c)

temp_r, temp_c = N-1, N-1
path = [(temp_r, temp_c)]

while best_path_from_start[temp_r][temp_c]['prev'] is not None:
    temp_r, temp_c = best_path_from_start[temp_r][temp_c]['prev']
    path.append((temp_r, temp_c))

path_queue = deque(path)

while path_queue:
    pathq_r, pathq_c = path_queue.popleft()
    left_cell = best_path_from_start[pathq_r][pathq_c]['prev']
    top_cell = None
    if 'prev2' in best_path_from_start[pathq_r][pathq_c]:
        top_cell = best_path_from_start[pathq_r][pathq_c]['prev2']
    
    if left_cell not in path and left_cell is not None:
        path.append(left_cell)
        path_queue.append(left_cell)
    if top_cell not in path and top_cell is not None:
        path.append(top_cell)
        path_queue.append(top_cell)

direct_path_value = best_path_from_start[N-1][N-1]['value']
side_path_value = -float('inf')

for (cell_r, cell_c) in path:
    if cell_r + cell_c + T > (N-1) + (N-1):
        continue
    
    best_path_from_cell = [[0 for _c in range(T+1)] for _r in range(T+1)]
    best_path_from_cell[0][0] = GRID[cell_r][cell_c]

    for t in range(1, T+1):
        if is_valid_coord(cell_r+t, cell_c):
            best_path_from_cell[t][0] = best_path_from_cell[t-1][0] + GRID[cell_r+t][cell_c]
        else:
            best_path_from_cell[t][0] = -float('inf')
        if is_valid_coord(cell_r, cell_c+t):
            best_path_from_cell[0][t] = best_path_from_cell[0][t-1] + GRID[cell_r][cell_c+t]
        else:
            best_path_from_cell[0][t] = -float('inf')

    for r in range(1, T+1):
        for c in range(1, T+1):
            from_left = best_path_from_cell[r][c-1]
            from_top = best_path_from_cell[r-1][c]
            if is_valid_coord(cell_r+r, cell_c+c):
                best_path_from_cell[r][c] = max(from_left, from_top) + GRID[cell_r+r][cell_c+c]

    cell_best_path = -float('inf')
    for r in range(0, T+1):
        c = T - r
        cell_best_path = max(cell_best_path, best_path_from_cell[r][c])

    side_path_value = max(side_path_value, cell_best_path)

answer = direct_path_value + max(0, side_path_value)
print(answer)