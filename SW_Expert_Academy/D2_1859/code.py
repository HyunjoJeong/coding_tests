## 1859. 백만장자 프로젝트
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc

## 전략: greedy algorithm
## 뒤에서부터 순회(reverse)하여 현재 최댓값보다 크면 update, 작으면 합산

N = int(input())
outputBuffer = []

## 입력
for i in range(N):
    count = int(input())
    prices = [int(x) for x in reversed(input().split())]

    sum = 0
    maxPrice = prices[0]

    for price in prices:
        if (price > maxPrice): maxPrice = price
        else: sum += maxPrice - price

    outputBuffer.append(sum)

## 출력
for i in range(N):
    print(f"#{i+1} {outputBuffer[i]}")
