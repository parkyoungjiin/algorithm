import sys

input = sys.stdin.readline

t = int(input())
dp = [[]] * (41)
# 인덱스 잘못 생각한 코드
# dp[0][0], dp[0][1] = 1,0
# dp[1][0], dp[1][1] = 0,1
# dp[2][0], dp[2][1] = 1,1

# 정답
dp[0] = [1,0]
dp[1] = [0,1]
dp[2] = [1,1]
for i in range(3, 41):
    # 인덱스 잘못 생각한 코드
    # dp[i][0], dp[i][1] = dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]
    dp[i] = [dp[i-1][0] + dp[i-2][0], dp[i-1][1] + dp[i-2][1]]


for _ in range(t):
    n = int(input())
    
    print(dp[n][0], dp[n][1])
        



