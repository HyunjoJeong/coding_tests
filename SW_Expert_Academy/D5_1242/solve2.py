## 1242. 암호코드 스캔
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15JEKKAM8CFAYD
## 전략: 각 줄의 앞에서부터 읽으면서 비율을 통해 코드 확인

# 16진수 -> 2진수 변환
hex_to_bin = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011',
    '4': '0100', '5': '0101', '6': '0110', '7': '0111',
    '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
    'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}

# 1, 0, 1 의 비율을 이용한 숫자 매핑 (맨 앞의 0은 생략)
ratio_to_num = {
    (2, 1, 1): 0, (2, 2, 1): 1, (1, 2, 2): 2, (4, 1, 1): 3,
    (1, 3, 2): 4, (2, 3, 1): 5, (1, 1, 4): 6, (3, 1, 2): 7,
    (2, 1, 3): 8, (1, 1, 2): 9
}

def solve():
    N, M = map(int, input().split())

    result = 0
    previousLine = ''
    checked_codes = set()

    for n in range(N):
        line = input().strip()
        if line == previousLine or line == '0' * M: continue

        binary_line = "".join([hex_to_bin[x] for x in line])
        previousLine = line
        index = 0

        while index < M * 4 - 56:
            if binary_line[index] == '0': index += 1; continue

            code = []
            for i in range(8):
                c1 = c2 = c3 = 0
                while binary_line[index] == '0': index += 1
                while binary_line[index] == '1': index += 1; c1 += 1
                while binary_line[index] == '0': index += 1; c2 += 1
                while index < M * 4 and binary_line[index] == '1': index += 1; c3 += 1

                k = min(c1, c2, c3)
                code.append(ratio_to_num[((c1//k, c2//k, c3//k))])

            code_tuple = tuple(code)

            if code_tuple not in checked_codes:
                odds = code_tuple[0] + code_tuple[2] + code_tuple[4] + code_tuple[6]
                evens = code_tuple[1] + code_tuple[3] + code_tuple[5] + code_tuple[7]

                if (odds * 3 + evens) % 10 == 0:
                    checked_codes.add(code_tuple)
                    result += odds + evens

    return result

T = int(input().strip())

for t in range(1, T+1):
    print(f"#{t} {solve()}")