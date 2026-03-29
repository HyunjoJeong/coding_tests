## 3752.
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWHPkqBqAEsDFAUn

## 전략: set로 풀면 될 듯

T = int(input())
outputBuffer = []

def solve():
    cases = set({0})

    for score in scores:
        newCases = set()
        for case in cases:
            newCases.add(case + score)
        cases.update(newCases)

    outputBuffer.append(len(cases))

## 입력
for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))

    solve()

## 출력
for t in range(T):
    print(f"#{t+1} {outputBuffer[t]}")