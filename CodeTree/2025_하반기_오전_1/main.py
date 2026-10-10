N, M = map(int, input().split())
GRID = [[0 for _c in range(N)] for _r in range(N)]

boxes = dict()      # key: 박스ID, value: [r,c,h,w] / 여기서 r,c는 좌측하단의 좌표값

def gravity():
    for k, box in boxes.items():
        r, c, h, w = box

        i = 0
        while True:
            i += 1
            if r+i >= N: break
            if any(GRID[r+i][c:c+w]): break
        i -= 1

        for _r in range(r, r-h, -1):
            for _c in range(c, c+w):
                GRID[_r][_c] = 0
                GRID[_r+i][_c] = k
        boxes[k] = [r+i, c, h, w]

# 1. 택배 투입
# h: 세로, w: 가로, c: 좌측좌표, 시작은 가능한 제일 위에서.
# 중력에 의해 하단으로 떨어지고, 바닥 or 다른 택배가 있으면 거기서 멈춤

def insert(k, h, w, c):
    """ GRID와 boxes에 신규 박스 등록 """
    for _r in range(0, h):
        for _c in range(c, c+w):
            GRID[_r][_c] = k
    boxes[k] = [h-1, c, h, w]

def step1():
    for m in range(M):
        k, h, w, c = map(int, input().split())  # k: 택배번호, h: 세로, w: 가로, c: 좌측 좌표
        insert(k, h, w, c-1)
        gravity()

# 2/3. 좌측/우측 택배 제거
# 좌/우로 뺄 수 있는 것 중 번호가 가장 작은 택배를 뺀다.
# 빼고 난 후 gravity

def is_left_removable(box):
    r, c, h, w = box

    for _r in range(r, r-h, -1):
        for _c in range(0, c):
            if GRID[_r][_c] > 0:
                return False
    return True

def is_right_removable(box):
    r, c, h, w = box

    for _r in range(r, r-h, -1):
        for _c in range(c+w, N):
            if GRID[_r][_c] > 0:
                return False
    return True

def remove(k):
    r, c, h, w = boxes[k]

    for _r in range(r, r-h, -1):
        for _c in range(c, c+w):
            GRID[_r][_c] = 0
    del boxes[k]
    print(k)

def step2():
    removable_boxes = []
    for k, box in boxes.items():
        if is_left_removable(box):
            removable_boxes.append(k)
    remove(min(removable_boxes))
    gravity()

def step3():
    removable_boxes = []
    for k, box in boxes.items():
        if is_right_removable(box):
            removable_boxes.append(k)
    remove(min(removable_boxes))
    gravity()

############################################################################

step1()

while boxes:
    step2()
    step3()