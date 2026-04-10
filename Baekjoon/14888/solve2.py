## 14888. 연산자 끼워넣기
## https://www.acmicpc.net/problem/14888
## 전략: BFS (loop)

from collections import deque

N = int(input().strip())
nums = list(map(int, input().strip().split()))
op_counts = list(map(int, input().strip().split()))

max_val = -float('inf')
min_val = float('inf')

def solve():
    global max_val, min_val
    queue = deque([(1, nums[0], *op_counts)]) # (연산 회차, 현재까지 계산 결과, plus, minus, multiply, divide)

    while queue:
        n, result, plus, minus, multiply, divide = queue.popleft()

        if n == N:
            max_val = max(max_val, result)
            min_val = min(min_val, result)
            continue

        if plus > 0:
            queue.append((n+1, result + nums[n], plus-1, minus, multiply, divide))
        if minus > 0:
            queue.append((n+1, result - nums[n], plus, minus-1, multiply, divide))
        if multiply > 0:
            queue.append((n+1, result * nums[n], plus, minus, multiply-1, divide))
        if divide > 0:
            next_result = result // nums[n] if result >= 0 else -(-result // nums[n])
            queue.append((n+1, next_result, plus, minus, multiply, divide-1))

solve()

print(max_val)
print(min_val)