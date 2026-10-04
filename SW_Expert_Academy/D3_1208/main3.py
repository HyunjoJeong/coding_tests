## 1208. Flatten
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh
## 풀이: 각 층별로 개수를 세서 한번에 연산

T = 10
answers = []

for t in range(T):
    N = int(input())
    floors = list(map(int, input().split()))

    counts_min = [0] * 101
    counts_max = [0] * 101

    for floor in floors:
        counts_min[floor] += 1
        counts_max[floor] += 1

    acc = 0

    for i in range(1, 101):
        acc += counts_min[i]
        counts_min[i+1] += counts_min[i]

        if acc > N:
            min_floor = i
            break
    
    acc = 0

    for i in range(100, 0, -1):
        acc += counts_max[i]
        counts_max[i-1] += counts_max[i]

        if acc > N:
            max_floor = i
            break
    
    answers.append(max_floor - min_floor)


for t in range(T):
    print(f"#{t+1} {answers[t]}")