## 14888. 연산자 끼워넣기
## https://www.acmicpc.net/problem/14888
## 전략: 재귀를 통한 DFS

N = int(input().strip())
nums = list(map(int, input().strip().split()))
op_counts = list(map(int, input().strip().split()))

max_val = -float('inf')
min_val = float('inf')

def dfs(idx, curr_result, plus, minus, multiply, divide):
    global max_val, min_val
    
    if idx == N:
        max_val = max(max_val, curr_result)
        min_val = min(min_val, curr_result)
        return

    if plus > 0:
        dfs(idx + 1, curr_result + nums[idx], plus - 1, minus, multiply, divide)
    if minus > 0:
        dfs(idx + 1, curr_result - nums[idx], plus, minus - 1, multiply, divide)
    if multiply > 0:
        dfs(idx + 1, curr_result * nums[idx], plus, minus, multiply - 1, divide)
    if divide > 0:
        next_res = curr_result // nums[idx] if curr_result >= 0 else -(-curr_result // nums[idx])
        dfs(idx + 1, next_res, plus, minus, multiply, divide - 1)

dfs(1, nums[0], *op_counts)

print(max_val)
print(min_val)