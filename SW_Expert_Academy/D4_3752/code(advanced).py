## 전략: Bitset을 이용한 풀이.. 솔직히 이런 걸 시험장에선 생각 못하니까 그냥 참고용으로만..

T = int(input())
for t in range(T):
    N = int(input())
    scores = list(map(int, input().split()))
    
    reachable = 1                       # bitset 초기화 (0번 비트만 1)
    for s in scores:
        reachable |= (reachable << s)   # 기존 가능 점수들 | (기존 점수들을 s만큼 이동시킨 결과)
    
    print(f"#{t+1} {bin(reachable).count('1')}")