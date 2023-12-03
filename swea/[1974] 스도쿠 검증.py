#스도쿠는 숫자퍼즐로, 가로 9칸 세로 9칸으로 이루어져 있는 표에 1 부터 9 까지의 숫자를 채워넣는 퍼즐이다.
# 같은 줄에 1 에서 9 까지의 숫자를 한번씩만 넣고, 3 x 3 크기의 작은 격자 또한, 1 에서 9 까지의 숫자가 겹치지 않아야 한다.
# 9 * 9 

# 3차원 행렬로 받기?
# 1. 행과 열에 있는 값들이 중복되는지 아닌지 체크
# 2. 3*3 행렬에 중복되는지 아닌지 체크.
# - for in range(0, 9, 3)
# - i % 3 ==0 and j % 3 == 0

# 스도쿠 검증 함수 생성
def checkSudoku(M):
    for i in range(9):
        row_num = [0] * 10
        col_num = [0] * 10
        for j in range(9):
            # 가로 검사
            row = M[i][j]
            # 세로 검사
            col = M[j][i]

            # 이미 사용된 숫자라면, 0을 리턴
            if row_num[row]: return 0
            if col_num[col]: return 0
            
            # 아니라면, row_num과 col_num의 각 숫자 위치를 1로 변경
            row_num[row] = 1
            col_num[col] = 1

            # 3x3 행렬 검사
            if i % 3 == 0 and j % 3 == 0:
                square = [0] * 10
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        num = M[r][c]
                        if square[num]: return 0
                        square[num] = 1
    
    # 반복문이 정상적으로 다 수행된다면, 올바른 스도쿠이므로 1을 리턴
    return 1

# 테스트 케이스 개수 T 입력
T = int(input())
for tc in range(1, T+1):
    # 검사를 위한 행렬 입력
    mat = [list(map(int, input().split())) for _ in range(9)]

    # checkSudoku() 함수를 사용해서 return 값을 result에 저장
    result = checkSudoku(mat)

    # 결과 출력
    print('#{} {}'.format(tc, result))







    





