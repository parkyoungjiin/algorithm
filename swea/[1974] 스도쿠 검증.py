#스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
# 9 * 9 

# 3차원 행렬로 받기?
# 1. 행과 열에 있는 값들이 중복되는지 아닌지 체크
# 2. 3*3 행렬에 중복되는지 아닌지 체크.

import sys
input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    # N = int(input())
    arr = [list(map(int,input().split())) for _ in range(9)]
    
    # 행과 열 체크

    


