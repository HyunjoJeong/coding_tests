## 1238. Contact
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD
## BFS

from collections import deque

T = 10
answers = []

for t in range(T):
    N, start_node = list(map(int, input().split()))
    second_line = list(map(int, input().split()))
    edges = [set() for _ in range(101)]

    for i in range(N//2):
        edges[second_line[2*i]].add(second_line[2*i+1])

    visited = [False] * 101
    queue = deque([(0, start_node)])
    connected = deque([])

    while queue:
        depth, node = queue.popleft()

        if visited[node]: continue
        visited[node] = True
        connected.append((depth, node))

        for next_node in edges[node]:
            queue.append((depth+1, next_node))

    answers.append(sorted(connected)[-1][1])

for t in range(T):
    print(f"#{t+1} {answers[t]}")