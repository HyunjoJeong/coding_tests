## 1220. Magnetic
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD

T = 10
answers = []

for t in range(T):
    S = int(input())
    rows = [list(map(int, input().split())) for _ in range(S)]
    cols = [[rows[_c][_r] for _c in range(S)] for _r in range(S)]

    count = 0

    for col in cols:
        is_N = False
        for c in col:
            if c == 1:
                is_N = True
                continue
            if is_N and c == 2:
                count += 1
                is_N = False

    answers.append(count)


for t in range(T):
    print(f"#{t+1} {answers[t]}")