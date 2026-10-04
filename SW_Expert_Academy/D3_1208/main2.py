## 1208. Flatten
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh
## 풀이: 각 층별로 개수를 세서 하나씩 줄이고 늘리기

T = 10
answers = []

for t in range(T):
    N = int(input())
    floors = list(map(int, input().split()))

    counts = [0] * 101
    for floor in floors:
        counts[floor] += 1

    top, bottom = max(floors), min(floors)

    for _ in range(N):
        if top - bottom <= 1: break

        counts[top] -= 1
        counts[top-1] += 1
        if counts[top] == 0: top -= 1

        counts[bottom] -= 1
        counts[bottom+1] += 1
        if counts[bottom] == 0: bottom += 1

    answers.append(top-bottom)


for t in range(T):
    print(f"#{t+1} {answers[t]}")