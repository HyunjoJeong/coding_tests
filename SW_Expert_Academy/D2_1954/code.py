## 1954. 달팽이 숫자
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

## 전략: 관성(momentum) 유지

N = int(input())
outputBuffer = []

## 이동방향. 우-하-좌-상 순서 (RIGHT = 0, DOWN = 1, LEFT = 2, TOP = 3)
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)

## 입력
for i in range(N):
    n = int(input())
    matrixSize = n * n
    matrix = [[0] * n for _ in range(n)]
    
    x = y = 0
    direction = 0

    for i in range(matrixSize):
        matrix[y][x] = i + 1
        (nx, ny) = (x + dx[direction], y + dy[direction])

        if (nx < 0 or nx == n or ny < 0 or ny == n or matrix[ny][nx] != 0):
            direction = (direction + 1) % 4
            (nx, ny) = (x + dx[direction], y + dy[direction])

        (x, y) = (nx, ny)

    outputBuffer.append(matrix)


## 출력
for i in range(N):
    print(f"#{i+1}")
    for row in outputBuffer[i]:
        print(*row)