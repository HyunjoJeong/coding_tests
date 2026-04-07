## 17471. 게리맨더링
## https://www.acmicpc.net/problem/17471
## 전략: BFS + binary string

from collections import deque

# N: 구역의 개수 / P: 각 구역별 인구수 / E: 각 구역별 인접구역 리스트
N = int(input().strip())
P = list(map(int, input().strip().split()))
E = [list(map(lambda x: int(x) - 1, input().strip().split()[1:])) for _ in range(N)]

minDiff = sum(P)
groupFound = False

def isConnected(group: list[int]):
    queue = deque([group[0]])
    visited = [group[0]]

    while queue:
        nodes = E[queue.popleft()]
        for node in nodes:
            if node in group and node not in visited:
                queue.append(node)
                visited.append(node)
    
    return len(group) == len(visited)

for n in range(1, 2**(N-1)):
    # binary string을 통해 1인 group과 0인 group을 분리
    binary = format(n, f"0{N}b")
    groupA = [i for i, x in enumerate(binary) if x == '1']
    groupB = [i for i, x in enumerate(binary) if x == '0']

    if isConnected(groupA) and isConnected(groupB):
        groupFound = True

        sumA = sum(P[i] for i in groupA)
        sumB = sum(P[i] for i in groupB)
        minDiff = min(abs(sumA - sumB), minDiff)
        if minDiff <= 1:
            break

print(minDiff if groupFound else -1)
