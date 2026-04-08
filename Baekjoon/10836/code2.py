## 10836. 여왕벌
## https://www.acmicpc.net/problem/10836
## 전략: 매일 계산을 수행하는 게 아니라, ones, twos가 되는 위치만 기억해두고 누적합으로 풀자.

# M: matrix 크기, N: 날짜
input = open(0).readline

M, N = map(int, input().strip().split())
G = M * 2 - 1

growth = [0 for _ in range(G)]
growth[0] = 1

for n in range(N):
    zeros, ones, twos = map(int, input().strip().split())

    if zeros < G: growth[zeros] += 1
    if twos: growth[zeros+ones] += 1

for g in range(1, G):
    growth[g] += growth[g-1]

row = " ".join(map(str, growth[M:]))

for m in range(M):
    first = str(growth[M-1-m])
    print(f"{first} {row}")