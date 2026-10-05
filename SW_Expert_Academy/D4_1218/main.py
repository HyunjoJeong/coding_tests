## 1218. 괄호 짝짓기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD

T = 10
answers = []
pairs = { ')': '(', ']': '[', '}': '{', '>': '<' }

for t in range(T):
    N = int(input())
    brackets = input().strip()

    if N % 2 == 1:
        answers.append(0)
        continue

    answer = 1
    stack = []

    for bracket in brackets:
        if bracket in '([{<':
            stack.append(bracket)
        elif not stack or stack.pop() != pairs[bracket]:
            answer = 0
            break

    answers.append(answer)

for t in range(T):
    print(f"#{t+1} {answers[t]}")