# https://www.codetree.ai/ko/frequent-problems/hsat/problems/grading/description

N = int(input())
scores = [list(map(int, input().split())) for _ in range(3)]

scores.append([])
for n in range(N):
    scores[3].append(scores[0][n] + scores[1][n] + scores[2][n])

def get_rank(score_list):
    sorted_list = sorted(score_list, reverse=True)
    order_map = dict()
    visited = set()

    for i, score in enumerate(sorted_list):
        if score not in visited:
            visited.add(score)
            order_map[score] = i + 1
        
    order_list = []

    for score in score_list:
        order_list.append(order_map[score])

    print(" ".join(map(str, order_list)))

for score_list in scores:
    get_rank(score_list)