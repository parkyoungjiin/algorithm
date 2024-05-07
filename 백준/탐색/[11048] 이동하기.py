import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

candy = []

dp = [[0 for _ in range(m)]for i in range(n)]

for _ in range(n):
    candy.append(list(map(int,input().split())))

dp[0][0] = candy[0][0]

for i in range(n):
    for j in range(m):
        if 0<=i+1<n:
            dp[i+1][j] = max(dp[i][j] + candy[i+1][j], dp[i+1][j])
        
        if 0<=j+1<m:
            dp[i][j+1] = max(dp[i][j] + candy[i][j+1],dp[i][j+1])

        if 0<=i+1<n and 0<=j+1<m:
            dp[i+1][j+1] = max(dp[i][j] + candy[i+1][j+1], dp[i+1][j+1])

print(max(max(dp)))





