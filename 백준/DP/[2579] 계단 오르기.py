import sys
input = sys.stdin.readline
n = int(input())

stairs = [0]
dp = [0] * (n+1)
for _ in range(n):
    stairs.append(int(input()))

if len(stairs) <= 2:
    print(sum(stairs))

else:
    dp[0] = 0
    dp[1] = stairs[1]
    dp[2] = dp[1] + stairs[2]


    for i in range(3, n+1):
        # dp[i] = max(계단 2칸 올라오기, 계단 1칸 올라오기)
        dp[i] = max(dp[i-2], dp[i-3] + stairs[i-1]) + stairs[i]

    print(dp[n])




