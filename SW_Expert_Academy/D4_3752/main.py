## 3752. 가능한 시험 점수
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn

T = int(input())
answers = []

for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))

    combs = set({ 0 })
    new_combs = set()

    for score in scores:
        for comb in combs:
            new_combs.add(comb + score)
        combs.update(new_combs)

    answers.append(len(combs))

for t in range(T):
    print(f"#{t+1} {answers[t]}")