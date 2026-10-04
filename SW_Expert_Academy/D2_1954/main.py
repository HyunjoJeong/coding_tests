## 1954. 달팽이 숫자
## https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5PobmqAPoDFAUq

T = int(input())
answers = []

# 우 하 좌 상
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def is_valid_coord(r: int, c: int, N: int):
  return 0 <= r < N and 0 <= c < N

for t in range(T):
  N = int(input())
  matrix = [[0 for _c in range(N)] for _r in range(N)]

  r = c = i = 0

  for n in range(N*N):
    matrix[r][c] = n + 1
    nr, nc = r + dr[i], c + dc[i]

    if not is_valid_coord(nr, nc, N) or matrix[nr][nc] != 0:
      i = (i + 1) % 4
      nr, nc = r + dr[i], c + dc[i]

    r, c = nr, nc

  answers.append(matrix)


for t in range(T):
  print(f"#{t+1}")
  for row in answers[t]:
    print(" ".join(map(str, row)))