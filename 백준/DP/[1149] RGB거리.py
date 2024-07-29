import sys

input = sys.stdin.readline

n = int(input())

dp = []
# dp = [[0,0,0] for _ in range(n)]
for _ in range(n):
    dp.append(list(map(int, input().split())))

for i in range(1, n):
    for j in range(n):
        if j == 0:
            dp[i][j] = min(dp[i][j] + dp[i-1][j+1], dp[i][j] + dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = min(dp[i][j] + dp[i-1][j-1], dp[i][j] + dp[i-1][j+1])
        elif j == 2:
            dp[i][j] = min(dp[i][j] + dp[i-1][j-2], dp[i][j] + dp[i-1][j-1])

print(min(dp[-1]))