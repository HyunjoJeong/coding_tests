## 1216. 미로1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD

## 전략: DFS + 방문한 곳은 1(진행 불가)로 변경 / 나아갈 수 있는 곳들을 DFS

N = 10
SIZE = 16
outputBuffer = []

def solve(x: int, y: int):
    global puzzle

    if puzzle[y][x] == 3:
        return 1
    
    queue = []
    puzzle[y][x] = 1
    
    if puzzle[y][x+1] != 1:
        queue.append((x+1, y))
    if puzzle[y+1][x] != 1:
        queue.append((x, y+1))
    if puzzle[y][x-1] != 1:
        queue.append((x-1, y))
    if puzzle[y-1][x] != 1:
        queue.append((x, y-1))

    for (nextX, nextY) in queue:
        if solve(nextX, nextY):
            return 1
    
    return 0

## 입력
for n in range(N):
    _ = input()
    puzzle = [list(map(int, input())) for _ in range(SIZE)]

    outputBuffer.append(solve(1, 1))


## 출력
for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")