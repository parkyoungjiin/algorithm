import sys
input = sys.stdin.readline


for _ in range(10):
    T = int(input())
    sum_list = []
    for _ in range(100):
        row = list(map(int,input().split()))
        sum_list.append(row)
    
    sum_row = []
    sum_col = []
    sum_cross= []
    for i in range(100):
        # 행 합계 계산
        row_val = sum(sum_list[i])
        sum_row.append(row_val)

        col_val = 0
        # 열 합계 계산.
        for j in range(100):
            col_val += sum_list[j][i]

        sum_col.append(col_val)
    cross_val = 0
    cross_val2 = 0
    # 대각선 합계 계산
    for i in range(100):
        cross_val += sum_list[i][i]
        cross_val2 += sum_list[i][99-i]

    max_col = max(sum_col)
    max_row = max(sum_row)
    answer = max(max_col, max_row, cross_val, cross_val2)

    print("#{} {}".format(T, answer))

