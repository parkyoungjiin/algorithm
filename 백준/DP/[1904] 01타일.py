import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(1000001)]

dp[1] = 1
dp[2] = 2
dp[3] = 3

for i in range(4, n+1):
    dp[i] = (dp[i-2] + dp[i-1]) % 15746

print(dp[n])