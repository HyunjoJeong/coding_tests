## 1859. 백만장자 프로젝트
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
## 풀이: 부분 최댓값

T = int(input())
answers = []

for t in range(T):
  N = int(input())
  prices = list(map(int, input().split()))

  total_profit = 0

  while prices:
    max_price = max(prices)
    max_index = prices.index(max_price)
    for i in range(max_index):
      sum += max_price - prices[i]
    prices = prices[max_index+1:]

  answers.append(sum)

for t in range(T):
  print(f"#{t+1} {answers[t]}")