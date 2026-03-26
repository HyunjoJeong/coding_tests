## 1251. 하나로
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15StKqAQkCFAYD

## 전략: 프림 알고리즘
import heapq

T = int(input())
outputBuffer = []

def getSqrdDist(i: int, j: int):
    return (xCoords[i] - xCoords[j]) ** 2 + (yCoords[i] - yCoords[j]) ** 2

def solve():
    iterCount = 0
    totalSqrdDist = 0
    visited = [False] * N
    minDists = [float('inf')] * N
    minDists[0] = 0

    # 우선순위 큐 (거리제곱, node index)
    pq = [(0, 0)]

    while pq:
        sqrdDist, currentNode = heapq.heappop(pq)

        if visited[currentNode]:
            continue

        iterCount += 1
        totalSqrdDist += sqrdDist
        visited[currentNode] = True

        if iterCount == N:
            break

        for nextNode in range(N):
            if not visited[nextNode]:
                sqrdDist = getSqrdDist(currentNode, nextNode)
                if sqrdDist < minDists[nextNode]:
                    minDists[nextNode] = sqrdDist
                    heapq.heappush(pq, (sqrdDist, nextNode))

    outputBuffer.append(round(E * totalSqrdDist))

## 입력
for t in range(T):
    N = int(input())
    xCoords = [int(x) for x in input().split()]
    yCoords = [int(y) for y in input().split()]
    E = float(input())

    solve()

## 출력
for t in range(T):
    print(f"#{t+1} {outputBuffer[t]}")