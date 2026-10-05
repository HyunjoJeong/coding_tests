## 1245. 균형점
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15MeBKAOgCFAYD

T = int(input())
answers = []

for t in range(T):
    N = int(input())
    input_line = list(map(int, input().split()))
    coords, masses = input_line[:N], input_line[N:]

    eq_points = []

    for n in range(1, N):
        iters = 0
        left, right = coords[n-1], coords[n]

        while True:
            iters += 1
            middle = (left + right) / 2
            left_forces = right_forces = 0

            for i in range(0, n):
                left_forces += masses[i] / (middle - coords[i]) ** 2
            for i in range(n, N):
                right_forces += masses[i] / (coords[i] - middle) ** 2

            if right_forces == left_forces or iters > 110:
                eq_points.append(f"{middle:.10f}")
                break
            
            if right_forces > left_forces: 
                right = middle
            else: left = middle

    answers.append(" ".join(eq_points))

for t in range(T):
    print(f"#{t+1} {answers[t]}")