## 1245. 균형점
## 전략: 이분 탐색

T = int(input().strip())
outputBuffer = []

# 입력
for t in range(T):
    N = int(input().strip())
    secondLine = list(map(int, input().split()))
    positions = secondLine[:N]
    masses = secondLine[N:]

    eqPositions = []

    for n in range(N-1):
        leftBound = positions[n]
        rightBound = positions[n+1]

        I = 103                 # 100회 정도 반복하면 정밀도가 2^-100 => 약 1E-10 이하
        for i in range(I):
            dx = (rightBound - leftBound) / 2
            x = leftBound + dx

            leftForce = 0
            rightForce= 0

            for nn in range(n+1):
                leftForce += masses[nn] / (x - positions[nn])**2
            for nn in range(n+1, N):
                rightForce += masses[nn] / (positions[nn] - x)**2

            if rightForce == leftForce or i == I-1:
                eqPositions.append(f"{x:.10f}")
                break
            if rightForce > leftForce:
                rightBound = x
            else:
                leftBound = x

    outputBuffer.append(" ".join(eqPositions))

# 출력
for t in range(T):
    print(f"#{t+1} {outputBuffer[t]}")