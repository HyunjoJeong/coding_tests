## 1859. 백만장자 프로젝트
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc
## 풀이: 역순회

T = int(input())
answers = []

for t in range(T):
  N = int(input())
  prices = list(map(int, reversed(input().split())))

  total_profit = 0
  max_price = prices[0]

  for price in prices:
    if price > max_price: max_price = price
    else: total_profit += max_price - price

  answers.append(total_profit)


for t in range(T):
  print(f"#{t+1} {answers[t]}")