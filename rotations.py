def print_arr(title, arr):
    print(f"# {title}")
    for row in arr: print(row)
    print("#" * 40)

base = [
    ['a', 'a', 'a', 'a'],
    ['b', 'b', 'b', 'b'],
    ['c', 'c', 'c', 'c'],
    ['d', 'd', 'd', 'd']
]

def rotate_left(arr):
    rr, cc = len(arr), len(arr[0])
    temp = [['' for r in range(rr)] for c in range(cc)]
    for r in range(rr):
        for c in range(cc):
            temp[cc-1-c][r] = arr[r][c]
    return temp

def rotate_right(arr):
    rr, cc = len(arr), len(arr[0])
    temp = [['' for r in range(rr)] for c in range(cc)]
    for r in range(rr):
        for c in range(cc):
            temp[c][rr-1-r] = arr[r][c]
    return temp

print_arr('base', base)
print_arr('left', rotate_left(base))
print_arr('right', rotate_right(base))