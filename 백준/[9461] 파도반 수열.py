import sys

input = sys.stdin.readline

dp = [0 for _ in range(101)]

dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(4, 101):
    dp[i] = dp[i-3] + dp[i-2]


tc = int(input())
for _ in range(tc):
    n = int(input())
    print(dp[n])
