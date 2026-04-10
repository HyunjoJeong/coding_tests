# 2025 하반기 오전 1번 문제

import heapq

N, M = map(int, input().split())
matrix = [[None for _c in range(N)] for _r in range(N)]

def gravity():
    floor = [N for _ in range(N)]

    for _r in range(N-1, -1, -1):
        for _c in range(N):
            if matrix[_r][_c] is None: continue
            if floor[_c] <= _r: continue

            k, h, w = matrix[_r][_c]
            minFloor = min(floor[_c:_c+w])

            if minFloor > _r:
                for _h in range(h):
                    for _w in range(w):
                        matrix[_r-_h][_c+_w] = None
                        matrix[minFloor-_h-1][_c+_w] = (k, h, w)
                for _w in range(w):
                    floor[_c+_w] = minFloor - h

for _m in range(M):
    bk, bh, bw, bc = map(int, input().split())
    for _h in range(bh):
        for _w in range(bw):
            matrix[_h][_w+bc-1] = (bk, bh, bw)
    gravity()

def removeLeft():
    maybeList = []
    candidate = [0, 0, 0, 0]    # (k, r, c, count)

    for _r in range(N):
        for _c in range(N):
            if matrix[_r][_c]:
                k, h, w = matrix[_r][_c]
                if h == 1:
                    heapq.heappush(maybeList, (k, _r, _c))
                    break
                if candidate[0] == k:
                    candidate[3] -= 1
                    if candidate[3] == 0:
                        heapq.heappush(maybeList, (k, _r, _c))
                    break
                else:
                    candidate = [k, _r, _c, h-1]
                    break

    removeTarget = maybeList[0]
    targetK, targetR, targetC = removeTarget
    _, h, w = matrix[targetR][targetC]

    for _h in range(h):
        for _w in range(w):
            matrix[targetR-_h][targetC+_w] = None

    print(targetK)

def removeRight():
    maybeList = []
    candidate = [0, 0, 0, 0]

    for _r in range(N):
        for _c in range(N-1, -1, -1):
            if matrix[_r][_c]:
                k, h, w = matrix[_r][_c]
                if h == 1:
                    heapq.heappush(maybeList, (k, _r, _c))
                    break
                if candidate[0] == k:
                    candidate[3] -= 1
                    if candidate[3] == 0:
                        heapq.heappush(maybeList, (k, _r, _c))
                    break
                else:
                    candidate = [k, _r, _c, h-1]
                    break

    removeTarget = maybeList[0]
    targetK, targetR, targetC = removeTarget
    _, h, w = matrix[targetR][targetC]

    for _h in range(h):
        for _w in range(w):
            matrix[targetR-_h][targetC-_w] = None

    print(targetK)

restCount = M

while True:
    removeLeft()
    restCount -= 1
    gravity()
    if restCount == 0: break
    removeRight()
    restCount -= 1
    gravity()
    if restCount == 0: break
