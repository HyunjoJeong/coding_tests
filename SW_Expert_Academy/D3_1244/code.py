## 1244. 최대 상금
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

## 전략: DFS + pruning(중복 경우의 수 가지치기)

N = int(input())
outputBuffer = []

def depthFirstSearch(depth: int):
    global maxValue
    currentValue = int("".join(valueAsList))

    if (currentValue, depth) in visited:
        return
    if (depth == exchangeCount): 
        maxValue = max(maxValue, currentValue)
        return
    
    visited.add((currentValue, depth))

    for i in range(valueLength):
        for j in range(i+1, valueLength):
            valueAsList[i], valueAsList[j] = valueAsList[j], valueAsList[i]
            depthFirstSearch(depth + 1)
            valueAsList[i], valueAsList[j] = valueAsList[j], valueAsList[i]

## 입력
for n in range(N):
    inputAsArray = input().split()

    valueAsList = list(inputAsArray[0])
    valueLength = len(valueAsList)
    exchangeCount = int(inputAsArray[1])

    maxValue = 0
    visited = set()

    depthFirstSearch(0)

    outputBuffer.append(maxValue)


## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")