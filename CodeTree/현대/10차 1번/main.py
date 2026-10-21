# https://www.codetree.ai/ko/frequent-problems/hsat/problems/road-repair-robot/description
# 전략: 가능한 범위의 patch 길이의 최대값 최소값을 구하고 binary search

import math
from collections import deque

N, K = map(int, input().split())
X = list(map(int, input().split()))

# nbk = N by K = N / K
nbk = math.ceil(N / K)
diff = set()
for i in range(len(X)-nbk+1):
    diff.add(X[i+nbk-1] - X[i])

# pl = patch_length
minpl = min(diff) + 1
maxpl = X[-1] - X[0] + 1

queue = deque(X)
answer_flag = False

while True:
    midpl = (minpl + maxpl) // 2

    for k in range(K):
        coverage = queue[0] + midpl - 1
        while queue and queue[0] <= coverage:
            queue.popleft()
        if not queue:
            break

    if queue:
        if midpl == minpl:
            print(maxpl)
            break
        minpl = midpl
    else:
        if midpl == minpl:
            print(minpl)
            break
        maxpl = midpl

    queue = deque(X)