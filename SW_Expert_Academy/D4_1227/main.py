## 1227. 미로2 (1226과 동일한데, SIZE만 100으로 증가 => 좀 더 효율화한 버전)
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14wL9KAGkCFAYD

T = 10
S = 100
answers = []

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    _ = input()
    maze = [[int(x) for x in list(input())] for _ in range(S)]

    start_node = ()
    destination = ()

    for r in range(1, S-1):
        for c in range(1, S-1):
            if maze[r][c] == 2: start_node = (r, c)
            if maze[r][c] == 3: destination = (r, c)

    answer = 0
    stack = [start_node]
    visited = [[False for _c in range(S)] for _r in range(S)]

    while stack:
        r, c = stack.pop()

        if visited[r][c]: continue
        if (r, c) == destination:
            answer = 1
            break

        visited[r][c] = True

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if maze[nr][nc] != 1 and not visited[nr][nc]: stack.append((nr, nc))

    answers.append(answer)

for t in range(T):
    print(f"#{t+1} {answers[t]}")