import sys
input = sys.stdin.readline

n = int(input())

dp = [[0] * 10 for _ in range(1001)]

for i in range(n):
    for j in range(10):
        if i == 0:
            dp[0][i] = 1
        
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

print(sum(dp[n-1]) % 10007)


