## 1210. Ladder 1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14ABYKADACFAYh

T = 10
answers = []

def is_left_avail():
    global x, y, ladder
    return x > 0 and ladder[y][x-1] == 1

def is_right_avail():
    global x, y, ladder
    return x < 99 and ladder[y][x+1] == 1

for t in range(T):
    _ = input()
    ladder = [list(map(int, input().split())) for _ in range(100)]

    x = ladder[-1].index(2)
    y = 99

    while y > 0:
        if is_left_avail():
            while is_left_avail():
                x -= 1
        elif is_right_avail():
            while is_right_avail():
                x += 1
        y -= 1

    answers.append(x)

for t in range(T):
    print(f"#{t+1} {answers[t]}")