# N x N 행렬이 주어질 때,

# 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.


# [제약 사항]

# N은 3 이상 7 이하이다.
import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    num_arr = [list(map(str,input().strip().split())) for _ in range(N)]

    # 90도 회전
    num_arr2 = [[0] * N for _ in range(N)]
    # 180도 회전
    num_arr3 = [[0] * N for _ in range(N)]
    # 270도 회전
    num_arr4 = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            num_arr2[i][j] = num_arr[N-1-j][i]
            num_arr3[i][j] = num_arr[N-1-i][N-1-j]
            num_arr4[i][j] = num_arr[j][N-1-i]
    print(f'#{tc}')

    for a1,a2,a3 in zip(num_arr2, num_arr3, num_arr4):
        a11 = ''.join(a1)
        a22 = ''.join(a2)
        a33 = ''.join(a3)
        print(a11, a22, a33)
    


