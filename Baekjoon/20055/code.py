## 20055. 컨베이어 벨트 위의 로봇
## https://www.acmicpc.net/problem/20055
## 전략: 실제 배열을 움직이지 않고, startIndex를 움직여서 풀기

N, K = map(int, input().strip().split())
N *= 2
B = list(map(int, input().strip().split()))

iterCount = 0
startIndex = 0
robots = []

def robotDown():
    global robots

    if robots and robots[0] == N//2 - 1:
        robots = robots[1:]

def stage1():
    global iterCount, startIndex
    
    iterCount += 1
    startIndex = (startIndex - 1) % N

    for i, robot in enumerate(robots):
        robots[i] += 1

    robotDown()


def stage2():
    for i, robot in enumerate(robots):
        nextRobot = robot + 1
        nextIndex = (startIndex + nextRobot) % N
        if B[nextIndex] > 0 and nextRobot not in robots:
            robots[i] = nextRobot
            B[nextIndex] -= 1

    robotDown()

def stage3():
    if B[startIndex] > 0 and 0 not in robots:
        B[startIndex] -= 1
        robots.append(0)

while B.count(0) < K:
    stage1()
    stage2()
    stage3()
    
print(iterCount)