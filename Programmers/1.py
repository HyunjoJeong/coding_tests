# https://school.programmers.co.kr/learn/courses/30/lessons/43162
# 네트워크

from collections import deque

def solution(n, computers):
    answer = 0
    connected = [False for _ in range(n)]
    unconnected_nodes = { x for x in range(n) }
    
    while unconnected_nodes:
        answer += 1
        start_node = connected.index(False)
        queue = deque([start_node])

        while queue:
            node = queue.popleft()

            if connected[node]:
                continue
            
            connected[node] = True
            unconnected_nodes.discard(node)

            for i, value in enumerate(computers[node]):
                if value == 1 and not connected[i]:
                    queue.append(i)
    
    return answer

print(solution(3, [[1, 1, 0],[1, 1, 0],[0, 0, 1]]))