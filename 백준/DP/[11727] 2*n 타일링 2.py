import sys
input = sys.stdin.readline

n = int(input())

dp = [] * (n+1)
dp[0] = 0
dp[1] = 1
