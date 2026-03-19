## 1231. 중위순회
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD

## 전략: left 재귀 -> 내꺼 출력 -> right 재귀

N = 10
outputBuffer = []

def solve(nodeIndex: int):
    if (nodeIndex == 0):
        return
    
    solve(left[nodeIndex])
    answer.append(nodes[nodeIndex])
    solve(right[nodeIndex])

## 입력
for n in range(N):
    nodesCount = int(input()) + 1
    nodes = [''] * nodesCount
    left = [0] * nodesCount
    right = [0] * nodesCount

    for i in range(1, nodesCount):
        line = input().split()

        nodes[i] = line[1]
        if len(line) > 2:
            left[i] = int(line[2])
            if len(line) > 3:
                right[i] = int(line[3])

    answer = []
    solve(1)
    outputBuffer.append(''.join(answer))

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")