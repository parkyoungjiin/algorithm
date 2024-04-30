import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[1 for _ in range(n+1)]for _ in range(n+1)] # 1로 초기화
# print(dp)
for i in range(2, n+1):
    for j in range(1, i):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]

print(dp[n][k]%10007)




















# def bino_coef(n,k):
#     # 2차원으로 받기
#     dp = [[0 for _ in range(k+1)]for _ in range(n+1)]
#     # print(dp)

#     # n이 0이 되는 경우와 k가 n이 되는 경우는 1로 처리
#     for i in range(n+1):
#         dp[i][0] = 1

#     for i in range(k+1):
#         dp[i][i] = 1

#     # 이항계수 3번 성질 이용하여 저장
#     for i in range(1, n+1):
#         for j in range(1, k+1):
#             dp[i][j] = dp[i-1][j] + dp[i-1][k-1]

#     return dp[n][k]
# print(bino_coef(n,k))