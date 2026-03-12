## 1218. 괄호 짝짓기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD

## 전략: stack push/pop

N = 10
outputBuffer = []

def solve(stream: str):
    stack = []
    isValid = 1
    pairs = { ')': '(', '}': '{', ']': '[', '>': '<' }

    for char in stream:
        if char in '({[<':
            stack.append(char)
        elif not stack or stack.pop() != pairs[char]:
            isValid = 0
            break

    if stack:
        isValid = 0
        
    outputBuffer.append(isValid)

## 입력
for n in range(N):
    inputLength = int(input())
    inputLine = input()

    solve(inputLine)

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")