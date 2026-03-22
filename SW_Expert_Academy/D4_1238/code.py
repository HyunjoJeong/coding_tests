## 1238. Contact
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD

## 전략: BFS (재귀호출 X: 함수 호출 메모리 오버헤드 방지)

N = 10
SIZE = 100
outputBuffer = []

def solve():
    global firstNode, nextNodes

    currentQueue = [firstNode]
    nextQueue = []

    depth = 0
    depths = [0] * (SIZE+1)
    visited = [False] * (SIZE+1)
    visited[firstNode] = True

    while currentQueue:
        for startNode in currentQueue:
            for nextNode in nextNodes[startNode]:
                if not visited[nextNode]:
                    visited[nextNode] = True
                    depths[nextNode] = depth + 1
                    nextQueue.append(nextNode)
        if not nextQueue:
            break
        currentQueue = nextQueue
        nextQueue = []
        depth += 1

    lastIndex = -1
    for i in range(SIZE, -1, -1):
        if depths[i] == depth:
            lastIndex = i
            break

    outputBuffer.append(lastIndex)

## 입력
for n in range(N):
    [count, firstNode] = [int(x) for x in input().split()]
    inputLine = [int(x) for x in input().split()]

    nextNodes = [[] for _ in range(SIZE+1)]
    for i in range(0, count, 2):
        if inputLine[i+1] not in nextNodes[inputLine[i]]:
            nextNodes[inputLine[i]].append(inputLine[i+1])

    solve()

## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")