
T = int(input().strip())
answers = []

for t in range(T):
    _ = input() # 첫번째 줄 입력은 테케 번호이므로 생략
    numbers = list(map(int, input().split()))
    counts = [0 for _ in range(101)]

    for number in numbers:
        counts[number] += 1

    maximum = max(counts)
    
    for i in range(100, -1, -1):
        if counts[i] == maximum:
            answers.append(i)
            break

for t in range(T):
    print(f"#{t+1} {answers[t]}")