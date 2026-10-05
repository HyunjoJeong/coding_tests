## 1215. 회문1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi

T = 10
S = 8
answers = []

for t in range(T):
    L = int(input())
    rows = [list(input()) for _ in range(S)]
    cols = [[rows[_c][_r] for _c in range(S)] for _r in range(S)]

    count = 0

    for row in rows:
        for i in range(0, S-L+1):
            corpus = row[i:i+L]
            if corpus == corpus[::-1]: count += 1

    for col in cols:
        for i in range(0, S-L+1):
            corpus = col[i:i+L]
            if corpus == corpus[::-1]: count += 1

    answers.append(count)

for t in range(T):
    print(f"#{t+1} {answers[t]}")