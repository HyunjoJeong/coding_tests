
# max를 찾아서 그 앞까진 전부 사고 max에 팔기를 반복

T = int(input())
output_buffer = []

for t in range(T):
    N = int(input().strip())
    prices = list(map(int, input().split()))
    acc = 0

    while prices:
        max_index = prices.index(max(prices))
        for i in range(max_index):
            acc += prices[max_index] - prices[i]
        prices = prices[max_index + 1:]

    output_buffer.append(acc)

for t in range(T):
    print(f"#{t+1} {output_buffer[t]}")