# https://www.codetree.ai/ko/frequent-problems/hsat/problems/car-test/description

N, Q = map(int, input().split())
E = sorted(list(map(int, input().split())))
M = [int(input()) for _ in range(Q)]

index = dict()
for i, e in enumerate(E):
    index[e] = i * (N-1-i)

for m in M:
    if m in index:
        print(index[m])
    else:
        print(0)