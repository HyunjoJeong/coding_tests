from collections import deque

N, M, K = map(int, input().split())

# { start_node : edges } => { k: [a, b, c] } 
G = dict()
for m in range(M):
    x, y = map(int, input().split())
    if x in G: G[x].append(y)
    else: G[x] = [y]

S = list(map(int, input().split()))

# { start_node: { end_node: distance } }
distances = dict()

for s in S:
    distances[s] = dict()
    queue = deque([(s, 0)])
    visited = [False for n in range(N+1)]

    while queue:
        node, dist = queue.popleft()

        if visited[node]:
            continue

        visited[node] = True
        distances[s][node] = dist

        if node in G:
            for next_node in G[node]:
                if not visited[next_node]:
                    queue.append((next_node, dist+1))

max_distance = float('inf')

for n in range(1, N+1):
    max_distance_to_this_cell = 0
    for distance_map in distances.values():
        if n not in distance_map:
            max_distance_to_this_cell = float('inf')
            break
        else:
            max_distance_to_this_cell = max(distance_map[n], max_distance_to_this_cell)
        
    if max_distance_to_this_cell > 0:
        max_distance = min(max_distance, max_distance_to_this_cell)

print(max_distance if max_distance != float('inf') else -1)