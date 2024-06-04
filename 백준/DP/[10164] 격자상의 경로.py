import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

dp = [[0]*m for _ in range(n)]

result = 1
# 동그라미 X
if k == 0:
    for i in range(n):
        for j in range(m):
            if (i==0 or j==0):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]

    result *= dp[n-1][m-1]
else:
    # 중간지점
    mid_x = (k-1) // m
    mid_y = (k-1) % m

    # 1번 ~ 중간
    for i in range(mid_x + 1):
        for j in range(mid_y + 1):
            if (i==0 or j ==0):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 중간까지 계산
    result *= dp[mid_x][mid_y]
    # 중간 ~ N*M
    for i in range(mid_x, n):
        for j in range(mid_y, m):
            if (i==mid_x or j==mid_y):
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    # 경로 결과
    result *= dp[n-1][m-1]
