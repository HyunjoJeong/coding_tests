## 1206. View (조망권 계산)
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh

## 전략: 주변 5칸을 기준으로 max 일때 (max-secondMax)를 누적합 / 최적화를 위해 max일 경우 n += 3

ITER_COUNT = 10     ## 10회 시행으로 주어짐
outputBuffer = []

## 입력
for i in range(ITER_COUNT):
    N = int(input())
    buildings = [int(x) for x in input().split()]

    n = 2
    niceViews = 0

    while True:
        if (n >= N-2): 
            outputBuffer.append(niceViews)
            break
        if (buildings[n] == max(buildings[n-2:n+3])):
            secondMax = max(buildings[n-2], buildings[n-1], buildings[n+1], buildings[n+2])
            niceViews += buildings[n] - secondMax
            n += 3
        else:
            n+= 1

## 출력
for i in range(ITER_COUNT):
    print(f"#{i+1} {outputBuffer[i]}")