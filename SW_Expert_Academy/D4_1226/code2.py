
T = 10
W = 16
output_buffer = []

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    input() # 첫줄 생략
    maze = [input() for _ in range(W)]

    start = (0, 0)
    destination = (0, 0)

    for r in range(W):
        for c in range(W):
            if maze[r][c] == '2': start = (r, c)
            elif maze[r][c] == '3': destination = (r, c)

    visited = [[False for _c in range(W)] for _r in range(W)]
    visited[start[0]][start[1]] = True
    stack = [start]
    answer = 0

    while stack:
        r, c = stack.pop()
        visited[r][c] = True

        if destination == (r, c):
            answer = 1
            break

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if maze[nr][nc] != '1' and not visited[nr][nc]:
                stack.append((nr, nc))

    output_buffer.append(answer)

for t in range(T):
    print(f"#{t+1} {output_buffer[t]}")