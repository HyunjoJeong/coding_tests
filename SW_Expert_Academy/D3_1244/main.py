## 1244. 최대 상금
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15Khn6AN0CFAYD

T = int(input())
answers = []

def dfs(count: int):
    global N, L, value_as_list, max_value, visited
    value = int("".join(value_as_list))

    if (count, value) in visited: return
    if count == N:
        max_value = max(max_value, value)
        return
    
    visited.add((count, value))

    for i in range(L-1):
        for j in range(i+1, L):
            value_as_list[i], value_as_list[j] = value_as_list[j], value_as_list[i]
            dfs(count+1)
            value_as_list[i], value_as_list[j] = value_as_list[j], value_as_list[i]

for t in range(T):
    init_value, N = list(map(int, input().split()))
    value_as_list = list(str(init_value))
    L = len(value_as_list)

    max_value = 0
    visited = set()

    dfs(0)

    answers.append(max_value)


for t in range(T):
    print(f"#{t+1} {answers[t]}")