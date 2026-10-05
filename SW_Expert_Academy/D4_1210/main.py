## 1210. Ladder 1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

T = 10
answers = []

def move(to: str):
    global direction, x, y

    if to == 'up':
        direction = 0
        y -= 1
    elif to == 'left':
        direction = -1
        x -= 1
    elif to == 'right':
        direction = 1
        x += 1


for t in range(T):
    _ = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    direction = 0 # -1(좌) 0(상) 1(우)
    x = ladder[-1].index(2)
    y = 99

    while y > 0:
        if direction == 0:
            if x > 0 and ladder[y][x-1] == 1: move('left')
            elif x < 99 and ladder[y][x+1] == 1: move('right')
            else: move('up')
        elif direction == -1:
            if x > 0 and ladder[y][x-1] == 1: move('left')
            else: move('up')
        elif direction == 1:
            if x < 99 and ladder[y][x+1] == 1: move('right')
            else: move('up')

    answers.append(x)


for t in range(T):
    print(f"#{t+1} {answers[t]}")