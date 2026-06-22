
# 더 진행할 수 없을 때 방향을 시계방향으로 변경 (우 하 좌 상)

T = int(input())
output_buffer = []

for t in range(T):
    N = int(input())
    matrix = [[0 for _c in range(N)] for _r in range(N)]

    r = c = dir = 0
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    for i in range(N ** 2):
        matrix[r][c] = i + 1
        nr, nc = r + dr[dir], c + dc[dir]

        if not (0 <= nr < N and 0 <= nc < N and matrix[nr][nc] == 0):
            dir = (dir + 1) % 4
            nr, nc = r + dr[dir], c + dc[dir]

        r, c = nr, nc

    output_buffer.append(matrix)

for t in range(T):
    print(f"#{t+1}")
    for row in output_buffer[t]:
        print(" ".join(map(str, row)))