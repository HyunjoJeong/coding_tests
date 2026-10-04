## 1206. View (조망권 계산)
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

T = 10
answers = []

for t in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))

    n = 2
    answer = 0

    while n < N-2:
        max_h = max(buildings[n-2], buildings[n-1], buildings[n+1], buildings[n+2])
        if buildings[n] > max_h:
            answer += buildings[n] - max_h
            n += 3
        else:
            n += 1

    answers.append(answer)


for t in range(T):
    print(f"#{t+1} {answers[t]}")