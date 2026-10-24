# https://www.codetree.ai/ko/frequent-problems/hsat/problems/supercomputer-cluster/description

N, B = map(int, input().split())
A = list(map(int, input().split()))

left = min(A)
right = B + max(A)

while True:
    if right - left <= 1:
        print(left)
        break
    
    mid = (left + right) // 2

    costs = 0
    for a in A:
        if mid > a:
            costs += (mid - a) ** 2
            if costs > B:
                break

    if costs > B:
        right = mid
    else:
        left = mid