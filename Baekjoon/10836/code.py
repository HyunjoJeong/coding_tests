## 10836. 여왕벌
## https://www.acmicpc.net/problem/10836
## 전략: 첫번째 열과 행만 계산. 어차피 첫번째 열이 아닌 모든 열은 첫번째 행의 값과 동일하기 때문
## 참고: 마지막 Testcase를 통과하지 못해 83점임.

# M: matrix 크기, N: 날짜
M, N = map(int, input().strip().split())

row = [1 for _ in range(M)]
col = [1 for _ in range(M)]

for n in range(N):
    zeros, ones, twos = map(int, input().strip().split())
    growth = [0] * zeros + [1] * ones + [2] * twos

    for m in range(M):
        col[M-1-m] += growth[m]
        row[m] += growth[M-1+m]

for m in range(M):
    row[0] = col[m]
    print(" ".join(map(str, row)))