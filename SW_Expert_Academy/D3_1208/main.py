## 1208. Flatten
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh
## 풀이: 덤프 횟수 내에서 

T = 10
answers = []

for t in range(T):
    N = int(input())
    floors = sorted(list(map(int, input().split())))

    minimum = maximum = 0
    baseline = floors[0]

    while True:
        acc = 0

        for floor in floors:
            if baseline > floor:
                acc += baseline - floor
            else: break

        if acc > N:
            minimum = baseline - 1
            break

        if acc == N:
            minimum = baseline
            break

        baseline += 1

    baseline = floors[-1]

    while True:
        acc = 0

        for floor in reversed(floors):
            if baseline < floor:
                acc += floor - baseline
            else: break

        if acc > N:
            maximum = baseline + 1
            break

        if acc == N:
            maximum = baseline
            break

        baseline -= 1

    answers.append(maximum-minimum)    


for t in range(T):
    print(f"#{t+1} {answers[t]}")