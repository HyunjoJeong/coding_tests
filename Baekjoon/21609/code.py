## 21609. 상어 중학교
## https://www.acmicpc.net/problem/21609
## 전략: BFS

from collections import deque

N, M = map(int, input().strip().split())
color = [list(map(int, input().strip().split())) for _ in range(N)]

Null = -2
Black = -1
Rainbow = 0

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

biggestGroup = []
noGroup = True
score = 0

#1 가장 큰 block group 찾기 (BFS)
def step1():
    global biggestGroup, noGroup
    visited = [[False for _c in range(N)] for _r in range(N)]
    compareData = (0, 0, 0, 0)          # (그룹 size, 무지개 block 갯수, 대표r, 대표c)
    biggestGroup.clear()
    noGroup = True

    for r in range(N):
        for c in range(N):
            if visited[r][c] or color[r][c] <= Rainbow: continue
            visited[r][c] = True

            groupSize = 1
            groupColor = color[r][c]

            rainbowBlockCount = 0
            visitedRainbowBlocks = []
            sameColorGroup = [(r, c)]
            path = deque([(r, c)])

            while path:
                pr, pc = path.popleft()
                for i in range(4):
                    nr, nc = pr + dr[i], pc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        if color[nr][nc] == Rainbow or color[nr][nc] == groupColor:
                            if color[nr][nc] == Rainbow:
                                rainbowBlockCount += 1
                                visitedRainbowBlocks.append((nr, nc))
                            if color[nr][nc] == groupColor:
                                sameColorGroup.append((nr, nc))
                            groupSize += 1
                            visited[nr][nc] = True
                            path.append((nr, nc))

            if groupSize > 1:
                noGroup = False
                minR, minC = sorted(sameColorGroup)[0]
                currentData = (groupSize, rainbowBlockCount, minR, minC)
                if currentData > compareData:
                    compareData = currentData
                    biggestGroup = sameColorGroup + visitedRainbowBlocks

            for (rr, rc) in visitedRainbowBlocks:       # 다른 곳에서도 rainbow block은 참조해야 하니까 visited 해제
                visited[rr][rc] = False

#2 가장 큰 block group 지우고 점수 획득
def step2():
    global score
    score += len(biggestGroup) ** 2
    for (r, c) in biggestGroup: 
        color[r][c] = Null

def gravity():
    global color
    for c in range(N):
        floor = N - 1
        for r in range(N - 1, -1, -1):
            if color[r][c] == Black:    # 검정 block은 고정. floor를 검정 위로 옮기기.
                floor = r - 1
                continue
            if color[r][c] >= Rainbow:  # 색이 있으면 floor 위치로 떨어지게하고 floor 한칸 올리기 / 빈칸(-2)이면 아무동작 X (처리생략)
                if r != floor:
                    color[floor][c] = color[r][c]
                    color[r][c] = Null
                floor -= 1

def rotateLeft():
    global color
    temp = [[0 for _c in range(N)] for _r in range(N)]
    for r in range(N):
        for c in range(N):
            temp[N-1-c][r] = color[r][c]
    color = temp

while True:
    step1()
    if noGroup: break
    step2()
    gravity()
    rotateLeft()
    gravity()

print(score)