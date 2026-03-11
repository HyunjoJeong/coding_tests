## 1210. Ladder 1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

## 전략: 2에서부터 역으로 

N = 10
SIZE = 100
outputBuffer = []

def solve():
    global ladder

    x = ladder[SIZE-1].index(2)
    y = SIZE - 1

    while y > 0:
        if (x > 0 and ladder[y][x-1] == 1):
            while (x > 0 and ladder[y][x-1] == 1):
                x -= 1
        elif (x < SIZE-1 and ladder[y][x+1] == 1):
            while (x < SIZE-1 and ladder[y][x+1] == 1):
                x += 1
        y -= 1
    
    outputBuffer.append(x)

## 입력
for n in range(N):
    tc_num = input()
    ladder = [list(map(int, input().split())) for _ in range(SIZE)]

    solve()

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")