## 1219. 길찾기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD

## 전략: DFS

N = 10
SIZE = 100
outputBuffer = []

def solve(node: int):
    global graph
    nextNodes = graph[node]

    if not nextNodes:
        return 0
    if 99 in nextNodes:
        return 1
    if len(nextNodes) == 1:
        return solve(nextNodes[0])
    return solve(nextNodes[0]) or solve(nextNodes[1])

## 입력
for n in range(N):
    edgeCount = int(input().split()[1])
    secondLine = input().split()

    graph = [[] for _ in range(SIZE)]

    for i in range(edgeCount * 2):
        if i % 2:
            graph[int(secondLine[i-1])].append(int(secondLine[i]))

    outputBuffer.append(solve(0))


## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")