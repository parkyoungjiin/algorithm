import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

pre_order_arr = []

# 입력 될때 동안 전위 그래프 완성
while True:
    try:
        pre_order_arr.append(int(input()))
    except:
        break

# 후위
def post_order(arr):
    if len(arr) == 0:
        return
    
    # 왼쪽 서브트리, 오른쪽 서브트리
    tempL, tempR = [], []

    root = arr[0]  
    for i in range(1, len(arr)):
        # 루트 값보다 큰 값인 경우(오른쪽 서브트리로 분류하고 종료)
        if arr[i] > root:
            tempL = arr[1:i]
            tempR = arr[i:]
            break

    else:
        tempL = arr[1:]
    # 후위니까 왼->오->루트 순으로 출력
    post_order(tempL)
    post_order(tempR)
    print(root)

post_order(pre_order_arr)

