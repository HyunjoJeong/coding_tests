## 1220. Magnetic
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14hwZqABsCFAYD

## 전략: 1 이후에 2가 나올 때마다 count 증가

N = 10
SIZE = 100
outputBuffer= []

for n in range(N):
    useless = input()
    rows = []
    columns = []

    for i in range(SIZE):
        rows.append([int(x) for x in input().split()])
    for i in range(SIZE):
        columns.append([x[i] for x in rows])

    count = 0

    for i in range(SIZE):
        isReady = False

        for j in range(SIZE):
            if (columns[i][j] == 1):
                isReady = True
                continue
            if (isReady and columns[i][j] == 2):
                count += 1
                isReady = False
    
    outputBuffer.append(count)

for n in range(N):
    print(f"#{n+1} {outputBuffer[n]}")