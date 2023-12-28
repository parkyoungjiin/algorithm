import sys
input = sys.stdin.readline

n = int(input())
# dp = 1로 만드는 최소 횟수
dp = [0] * (n+1)
answer = []
if n >= 2:
    for i in range(2, n+1):
        # 1로 뺴는 연산을 먼저 수행.
        dp[i] = dp[i-1] + 1
        # 만약 2로 나눠지거나, 3으로 나눠지는 경우가 더 연산 횟수가 적을 수 있기에 min 수행.
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1)
        if i % 3 == 0:
            dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[n])

result = [n]
now = n
# temp => n에서 -1한 값의 dp(최소 연산)
temp = dp[n] -1
# 1씩 내려가면서 순서 찾기.
for i in range(n, 0, -1):
    if dp[i] == temp and (i+1 == now or i*2 == now or i*3 == now):
        now = i
        result.append(i)
        temp -= 1
print(result)


