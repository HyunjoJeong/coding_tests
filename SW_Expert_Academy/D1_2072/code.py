## 2072. 홀수만 더하기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5QSEhaA5sDFAUq

count = int(input())
outputBuffer = []

## 입력 및 처리
for i in range(count):
    inputAsArray = input().split()
    sum = 0
    for j in inputAsArray:
        value = int(j)
        if (value % 2 == 1):
            sum += value
    outputBuffer.append(sum)

## 출력
for i in range(count):
    print(f"#{i+1} {outputBuffer[i]}")