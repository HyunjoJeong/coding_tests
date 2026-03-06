## 1208. Flatten
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV139KOaABgCFAYh

## 전략: 필요할 때마다 sort

N = 10
outputBuffer = []

## 입력
for i in range(N):
    n = int(input())
    numbers = sorted([int(x) for x in input().split()])

    for j in range(n):
        numbers[0] += 1
        numbers[-1] -= 1
        if (numbers[0] > numbers[1] or numbers[-2] > numbers[-1]):
            numbers.sort()
    
    outputBuffer.append(numbers[-1] - numbers[0])

## 출력
for i in range(N):
    print(f"#{i+1} {outputBuffer[i]}")