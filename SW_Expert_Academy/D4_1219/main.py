## 1219. 길찾기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD

T = 10
answers = []

for t in range(T):
    N = int(input().split()[1])
    routes = list(map(int, input().split()))
    route1 = [0] * 100
    route2 = [0] * 100

    for n in range(N):
        if route1[routes[2*n]] == 0:
            route1[routes[2*n]] = routes[2*n+1]
        else:
            route2[routes[2*n]] = routes[2*n+1]

    answer = 0
    stack = []
    visited = [False] * 100

    if route1[0]: stack.append(route1[0])
    if route2[0]: stack.append(route2[0])

    while stack:
        node = stack.pop()

        if visited[node]: continue
        if node == 99: 
            answer = 1
            break

        visited[node] = True

        if route1[node]: stack.append(route1[node])
        if route2[node]: stack.append(route2[node])

    answers.append(answer)

for t in range(T):
    print(f"#{t+1} {answers[t]}")