## 1227. 미로2 (1226과 동일한데, SIZE만 100으로 증가 => 좀 더 효율화한 버전)
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14wL9KAGkCFAYD

## 전략: DFS + 방문한 곳은 1(진행 불가)로 변경 / recursion 대신 stack을 통해 반복 search 하여 효율 높이기.

N = 10
SIZE = 100
outputBuffer = []

def solve():
    global puzzle
    stack = [(1,1)]

    while stack:
        x, y = stack.pop()

        if puzzle[y][x] == 3:
            return 1
        
        puzzle[y][x] = 1

        if puzzle[y][x+1] != 1:
            stack.append((x+1, y))
        if puzzle[y+1][x] != 1:
            stack.append((x, y+1))
        if puzzle[y][x-1] != 1:
            stack.append((x-1, y))
        if puzzle[y-1][x] != 1:
            stack.append((x, y-1))

    return 0

## 입력
for n in range(N):
    _ = input()
    puzzle = [list(map(int, input())) for _ in range(SIZE)]

    outputBuffer.append(solve())


## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")