# https://www.codetree.ai/ko/frequent-problems/hsat/problems/commute/description

from collections import deque

N, M = map(int, input().split())

next_map = dict()
prev_map = dict()
for _ in range(M):
    p, n = map(int, input().split())
    if p in next_map: next_map[p].append(n)
    else:             next_map[p] = [n]
    if n in prev_map: prev_map[n].append(p)
    else:             prev_map[n] = [p]

S, T = map(int, input().split())

def find_all_reachables(start, ignore, graph):
    reachables = set()

    visited = [False for _ in range(N+1)]
    queue = deque([start])

    while queue:
        node = queue.popleft()

        if visited[node]: continue
        if node == ignore: continue

        visited[node] = True
        reachables.add(node)

        if node in graph:
            for next_node in graph[node]:
                if not visited[next_node]:
                    queue.append(next_node)

    reachables.discard(start)
    return reachables

S2T = find_all_reachables(S, T, next_map) & find_all_reachables(T, -1, prev_map)
T2S = find_all_reachables(T, S, next_map) & find_all_reachables(S, -1, prev_map)

print(len(S2T & T2S))
