## 2819. 격자판의 숫자 이어 붙이기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB
## DP로 풀자

T = int(input())
S = 4
answers = []

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    grid = [input().split() for _ in range(S)]
    memo = [[[set() for _c in range(S)] for _r in range(S)] for _ in range(7)]

    for r in range(S):
        for c in range(S):
            memo[0][r][c].add(grid[r][c])

    for d in range(1, 7):
        for r in range(S):
            for c in range(S):
                for i in range(4):
                    nr, nc = r + dr[i], c + dc[i]
                    if nr < 0 or nr >= S or nc < 0 or nc >= S: continue
                    for combination in memo[d-1][nr][nc]:
                        memo[d][r][c].add(combination + grid[r][c])

    total = set()
    for r in range(S):
        for c in range(S):
            total.update(memo[6][r][c])

    answers.append(len(total))

for t in range(T):
    print(f"#{t+1} {answers[t]}")

