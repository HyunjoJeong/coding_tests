# 2025 상반기 오전 1번 문제

[N, T] = list(map(int, input().split()))
F = [list(map(str, input())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

representatives = []

def morning():
    for r in range(N):
        for c in range(N):
            B[r][c] += 1

def lunch():
    visited = [[False for _c in range(N)] for _r in range(N)]
    foodGroup = { 'T': 3, 'C': 3, 'M': 3, 'CM': 2, 'MT': 2, 'CT': 2, 'CMT': 1 }

    for r in range(N):
        for c in range(N):
            if visited[r][c]: continue

            visited[r][c] = True
            currentGroup = [(B[r][c], N-r, N-c)]    # max로 추출할 때 r, c는 작은 순으로 가져오기 위해.
            searchTree = [(r, c)]

            # 상하좌우
            dr = [-1, 1, 0, 0]
            dc = [0, 0 ,-1, 1]
            while searchTree:
                tr, tc = searchTree.pop()
                for i in range(4):
                    nr = tr + dr[i]
                    nc = tc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and F[nr][nc] == F[tr][tc]:
                        currentGroup.append((B[nr][nc], N-nr, N-nc))
                        searchTree.append((nr, nc))
                        visited[nr][nc] = True

            representativeIndex = currentGroup.index(max(currentGroup))
            for i, student in enumerate(currentGroup):
                sr, sc = N-student[1], N-student[2]
                if i == representativeIndex:
                    B[sr][sc] += len(currentGroup) - 1
                    representatives.append((foodGroup[F[sr][sc]], B[sr][sc], N-sr, N-sc))
                else:
                    B[sr][sc] -= 1

    representatives.sort(reverse=True)

def night():
    protected = []
    for representative in representatives:
        rr, rc = N-representative[2], N-representative[3]
        if (rr, rc) in protected: continue

        x = B[rr][rc] - 1
        i = B[rr][rc] % 4
        B[rr][rc] = 1

        # 상하좌우
        dr = [-1, 1, 0, 0]
        dc = [0, 0 ,-1, 1]
        nr, nc = rr, rc
        while x > 0:
            nr += dr[i]
            nc += dc[i]
            if nr < 0 or nr >= N or nc < 0 or nc >= N: break
            if F[nr][nc] == F[rr][rc]: continue

            protected.append((nr, nc))
            y = B[nr][nc]

            if x > y:                       # 강한 전파
                x -= (y + 1)
                F[nr][nc] = F[rr][rc]
                B[nr][nc] += 1
            else:                           # 약한 전파
                favors = set()
                for f in F[nr][nc]: favors.add(f)
                for f in F[rr][rc]: favors.add(f)
                F[nr][nc] = "".join(sorted(favors))
                B[nr][nc] += x
                x = 0

    belief = { 'CMT': 0, 'CT': 0, 'MT': 0, 'CM': 0, 'M': 0, 'C': 0, 'T': 0 }    # 민트초코우유, 민트초코, 민트우유, 초코우유, 우유, 초코, 민트
    for r in range(N):
        for c in range(N):
            belief[F[r][c]] += B[r][c]
    
    print(" ".join(list(map(str, belief.values()))))
    representatives.clear()

for t in range(T):
    morning()
    lunch()
    night()