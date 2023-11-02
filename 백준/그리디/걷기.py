X, Y, W, S = map(int, input().split())

min_time = 0
x, y = 0,0
# S = W*2 , S는 X, Y를 각각 1씩 증가.

if W >= S:
    print("가로지르는 것이 유리")
    # x, y가 X, Y를 초과하지 않도록.
else:
    if W*2 > S:
        print("가로질러")
    else:
        print("블럭이동")

while True:
    if x == X and y == Y:
        break;
    else:
        # 계산.