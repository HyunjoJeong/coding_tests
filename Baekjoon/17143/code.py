## 17143. 낚시왕
## https://www.acmicpc.net/problem/17143
## 전략: 

R, C, M = map(int, input().strip().split())
matrix = [[0 for _c in range(C)] for _r in range(R)]

# matrix에 초기 상어 정보 입력 (속도, 방향, 크기) / 방향 - (0: 상, 1: 하, 2: 우, 3: 좌)
for i in range(M):
    r, c, s, d, z = map(int, input().strip().split())
    matrix[r-1][c-1] = (s, d-1, z)

# 1. 낚시왕이 오른쪽으로 한 칸 이동한다. (낚시왕은 처음에 matrix 왼쪽 밖에 있고, 우측 밖으로 나가면 종료.)
# 2. 낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
# 3. 상어가 이동한다.

totalWeight = 0

def fishing(c: int):
    global totalWeight
    for r in range(R):
        if matrix[r][c]:
            totalWeight += matrix[r][c][2]
            matrix[r][c] = 0
            return
        
def sharkMove(startR: int, startC: int, speed: int, direction: int):
    nextR = startR + speed if direction == 1 else startR - speed if direction == 0 else startR
    nextC = startC + speed if direction == 2 else startC - speed if direction == 3 else startC
    nextD = direction

    modR = 2 * (R - 1)
    modC = 2 * (C - 1)

    nextR = nextR % modR
    nextC = nextC % modC

    if nextR >= R: nextR = modR - nextR; nextD = 1 - nextD
    if nextC >= C: nextC = modC - nextC; nextD = 5 - nextD

    return (nextR, nextC, nextD)

def allSharkMove():
    global matrix
    temp = [[0 for _c in range(C)] for _r in range(R)]
    for r in range(R):
        for c in range(C):
            if matrix[r][c]:
                s, d, z = matrix[r][c]
                nextR, nextC, nextD = sharkMove(r, c, s, d)
                if not temp[nextR][nextC] or temp[nextR][nextC][2] < z:
                    temp[nextR][nextC] = (s, nextD, z)
    matrix = temp

for ic in range(C):
    fishing(ic)
    allSharkMove()

print(totalWeight)