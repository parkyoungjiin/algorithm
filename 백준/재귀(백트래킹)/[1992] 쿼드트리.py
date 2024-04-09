import sys

n = int(input())
arr = []

for _ in range(n):
    arr.append(list(map(int,input())))

def solution(x, y, n):
    val = arr[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if val != arr[i][j]:
                val = -1
                break
    # -1 -> 다른 경우
    if val == -1:
        print("(",end='')
        # 4등분
        n = n //2
        solution(x, y, n) # 1사분면
        solution(x, y + n, n) # 2사분면
        solution(x + n, y, n) # 3사분면
        solution(x + n, y + n, n) # 4사분면 
        print(")",end='')

    elif val == 1:
        print(1, end='')
    else:
        print(0, end='')



solution(0, 0, n)