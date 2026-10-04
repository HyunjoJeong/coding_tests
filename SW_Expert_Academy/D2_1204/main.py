## 1204. 최빈수 구하기
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV13zo1KAAACFAYh

T = int(input())
answers = []

for t in range(T):
  _ = input()
  nums = list(map(int, input().split()))

  counts = [0] * 101

  for n in nums:
    counts[n] += 1

  max_count = max_num = 0

  for i, count in enumerate(counts):
    if count >= max_count:
      max_count = count
      max_num = i

  answers.append(max_num)

for t in range(T):
  print(f"#{t+1} {answers[t]}")