
T = 10
output_buffer = []

for t in range(T):
    N = int(input())
    buildings = list(map(int, input().split()))

    n = 2
    count = 0

    while n < N - 2:
        maximum = max(buildings[n-2], buildings[n-1], buildings[n+1], buildings[n+2])

        if buildings[n] > maximum:
            count += buildings[n] - maximum
            n += 3
        else:
            n += 1

    output_buffer.append(count)

for t in range(T):
    print(f"#{t+1} {output_buffer[t]}")