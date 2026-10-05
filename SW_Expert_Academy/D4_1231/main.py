## 1231. 중위순회
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV140YnqAIECFAYD

T = 10
answers = []

def in_order_search(node: int):
    global N, chars
    if node >= N: return ''
    return in_order_search(node*2+1) + chars[node] + in_order_search(node*2+2)

for t in range(T):
    N = int(input())
    chars = [input().split()[1] for _ in range(N)]

    answers.append(in_order_search(0))

for t in range(T):
    print(f"#{t+1} {answers[t]}")