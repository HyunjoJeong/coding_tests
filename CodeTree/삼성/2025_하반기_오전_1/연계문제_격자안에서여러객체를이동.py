# 2025 하반기 오전 1번 문제의 연계문제 - 격자 안에서 여러 객체를 이동
# https://www.codetree.ai/ko/trails/complete/curated-cards/intro-move-to-max-adjacent-cell-simultaneously/description

N, M, T = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(N)]
marbles = [tuple(map(lambda x: int(x)-1, input().split())) for _ in range(M)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for t in range(T):
    counts = [[0 for _c in range(N)] for _r in range(N)]

    for (r, c) in marbles:
        coordinate = (0, 0)
        maxValue = 0

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if not (0 <= nr < N and 0 <= nc < N): continue
            if G[nr][nc] > maxValue:
                maxValue = G[nr][nc]
                coordinate = (nr, nc)

        counts[coordinate[0]][coordinate[1]] += 1

    nextMarbles = []
    for _r in range(N):
        for _c in range(N):
            if counts[_r][_c] == 1:
                nextMarbles.append((_r, _c))

    marbles = nextMarbles
    if not nextMarbles: break

print(len(marbles))