## 1204. 최빈수 구하기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

## 전략: naive

T = int(input())
outputBuffer = []

GRADE_RANGE = 101

## 입력
for i in range(T):
    executeId = input()
    numbers = [int(x) for x in input().split()]

    table = [0] * GRADE_RANGE
    for number in numbers:
        table[number] += 1

    maxFrequency = 0
    result = 0

    for j in range(GRADE_RANGE):
        if (table[j] >= maxFrequency):
            maxFrequency = table[j]
            result = j

    outputBuffer.append((executeId, result))


## 출력
for i in range(T):
    print(f"#{outputBuffer[i][0]} {outputBuffer[i][1]}")