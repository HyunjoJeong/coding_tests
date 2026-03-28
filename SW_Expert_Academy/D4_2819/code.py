## 2819. 격자판의 숫자 이어 붙이기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV7I5fgqEogDFAXB

## 전략: DP

N = int(input())
outputBuffer = []

def solve():
    SIZE = 4
    LENGTH = 7

    memo = [[[set() for c in range(SIZE)] for r in range(SIZE)] for l in range(LENGTH)]
    for r in range(SIZE):
        for c in range(SIZE):
            memo[0][r][c].add(matrix[r][c])

    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    for l in range(1, LENGTH):
        for r in range(SIZE):
            for c in range(SIZE):
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < SIZE and 0 <= nc < SIZE:
                        for string in memo[l-1][nr][nc]:
                            memo[l][r][c].add(matrix[r][c] + string)

    totalSet = set()
    for r in range(SIZE):
        for c in range(SIZE):
            for string in memo[LENGTH-1][r][c]:
                totalSet.add(string)

    outputBuffer.append(len(totalSet))

## 입력
for n in range(N):
    matrix = [input().split() for _ in range(4)]
    solve()

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")