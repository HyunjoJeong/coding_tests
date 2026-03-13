## 1219. 길찾기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD

## 전략: DFS

N = 10
SIZE = 100
outputBuffer = []

def solve(node: int):
    global graph, visited
    
    visited[node] = True
    nextNodes = graph[node]

    if 99 in nextNodes:
        return 1
    for nextNode in nextNodes:
        if not visited[nextNode] and solve(nextNode):
            return 1
    return 0

## 입력
for n in range(N):
    edgeCount = int(input().split()[1])
    secondLine = input().split()

    visited = [False] * SIZE
    graph = [[] for _ in range(SIZE)]

    for i in range(edgeCount * 2):
        if i % 2:
            graph[int(secondLine[i-1])].append(int(secondLine[i]))

    outputBuffer.append(solve(0))

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")