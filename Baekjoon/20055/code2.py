from collections import deque

N, K = map(int, input().strip().split())
belt = deque(map(int, input().strip().split()))
robots = deque([False for _ in range(N)])
iterCount = 0

def stage1():
    belt.rotate()
    robots.rotate()
    robots[N-1] = False

def stage2():
    for i in range(N-2, -1, -1):
        if robots[i] and not robots[i+1] and belt[i+1] > 0:
            belt[i+1] -= 1
            robots[i] = False
            robots[i+1] = True
    robots[N-1] = False

def stage3():
    if belt[0] > 0 and not robots[0]:
        belt[0] -= 1
        robots[0] = True

while belt.count(0) < K:
    iterCount += 1
    stage1()
    stage2()
    stage3()

print(iterCount)