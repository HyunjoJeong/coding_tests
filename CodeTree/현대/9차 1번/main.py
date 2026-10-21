# https://www.codetree.ai/ko/frequent-problems/hsat/problems/security-manager/description
# 전략: ')' 발견시, 앞에 '(' 중 가장 마지막을 제거

N = int(input())
records = list(input())

def convert_edge():
    if records and records[0] == '?':
        records[0] = '('
    if records and records[-1] == '?':
        records[-1] = ')'

if N % 2 == 1:
    print('No')
else:
    while records:
        if records[0] == ')' or records[-1] == '(':
            print('No')
            break

        convert_edge()

        # loi: last_opener_index / fci: first_closer_index
        loi = 0
        fci = records.index(')')
        for i in range(fci-1, -1, -1):
            if records[i] == '(':
                loi = i
                break
        records = records[:loi] + records[loi+1:fci] + records[fci+1:]
    
    if not records:
        print('Yes')