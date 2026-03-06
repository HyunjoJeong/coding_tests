## 1215. 회문1
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi

## 전략: naive하게 각 행/열마다 n번 check

N = 10
outputBuffer = []

WIDTH = 8

def checkPalindrome(array):
    return array == array[::-1]

## 입력
for i in range(N):
    rows = []
    columns = []
    length = int(input())

    for j in range(WIDTH):
        rows.append(list(map(str, input())))
    for j in range(WIDTH):
        columns.append([row[j] for row in rows])

    count = 0

    for j in range(WIDTH):
        for k in range(WIDTH - length + 1):
            if (checkPalindrome(rows[j][k:k+length])):
                count += 1
            if (checkPalindrome(columns[j][k:k+length])):
                count += 1

    outputBuffer.append(count)

## 출력
for i in range(N):
    print(f"#{i+1} {outputBuffer[i]}")
