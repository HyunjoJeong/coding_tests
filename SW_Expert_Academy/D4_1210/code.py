## 1210. Ladder 1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

## 전략: 2에서부터 역으로 

N = 10
SIZE = 100
outputBuffer = []

UP = 0; LEFT = 1; RIGHT = 2

def solve():
    global ladder

    x = ladder[SIZE-1].index(2)
    y = SIZE - 1
    dir = UP

    while y != 0:
        y_up = y - 1
        x_left = x - 1
        x_right = x + 1

        if dir == UP:
            if (x_left >= 0 and ladder[y][x_left] == 1):
                dir = LEFT
                x = x_left
            elif (x+1 < SIZE and ladder[y][x_right] == 1):
                dir = RIGHT
                x = x_right
            else:
                y = y_up
        elif dir == LEFT:
            if ladder[y_up][x]:
                dir = UP
                y = y_up
            else:
                x = x_left
        elif dir == RIGHT:
            if ladder[y_up][x]:
                dir = UP
                y = y_up
            else:
                x = x_right
    
    outputBuffer.append(x)

## 입력
for n in range(N):
    _ = input()
    ladder = []

    for s in range(SIZE):
        ladder.append(list(map(int, input().split())))

    solve()

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")