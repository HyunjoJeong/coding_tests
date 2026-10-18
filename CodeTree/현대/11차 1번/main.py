# https://www.codetree.ai/ko/frequent-problems/hsat/problems/check-digital-logic-pattern/description
# 전략: K 길이의 pattern을 숫자로 치환해 hashmap의 key로 설정. 다음 해쉬 계산은 매번 전체 계산하지 않고, 하나빼고 추가하는 식으로.

S = input()
K, M = map(int, input().split())

pattern = int(S[0:K], 2)
combinations = dict()
output = 0

for i in range(K, len(S)):
    pattern = pattern * 2 - (int(S[i-K]) * 2 ** K) + int(S[i])
    if pattern in combinations:
        combinations[pattern] += 1
        if combinations[pattern] >= M:
            output = 1
            break
    else:
        combinations[pattern] = 1

print(output)