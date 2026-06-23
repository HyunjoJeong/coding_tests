
from collections import deque

T = 10
output_buffer = []

for t in range(T):
    edge_counts = int(input().split()[1])
    edge_rawdata = list(map(int, input().split()))
    edge1 = [0 for _ in range(100)]
    edge2 = [0 for _ in range(100)]

    for i in range(edge_counts):
        start, end = edge_rawdata[2*i], edge_rawdata[2*i+1]
        if edge1[start] == 0:
            edge1[start] = end
        else:
            edge2[start] = end

    answer = 0
    queue = deque()
    visited = [False for _ in range(100)]

    if edge1[0]: queue.append(edge1[0])
    if edge2[0]: queue.append(edge2[0])

    while queue:
        node = queue.popleft()
        visited[node] = True

        if node == 99:
            answer = 1
            break

        if edge1[node] and not visited[edge1[node]]: queue.append(edge1[node])
        if edge2[node] and not visited[edge2[node]]: queue.append(edge2[node])

    output_buffer.append(answer)
    
for t in range(T):
    print(f"#{t+1} {output_buffer[t]}")
