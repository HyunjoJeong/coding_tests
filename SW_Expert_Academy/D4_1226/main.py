## 1226. 미로1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD
## DFS

T = 10
S = 16
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