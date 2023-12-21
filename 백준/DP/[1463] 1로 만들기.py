import sys
input = sys.stdin.readline
n = int(input())
cnt = 0 

dp = [0] * 1000001
# dp[0] = 0, dp[1] = 0
for i in range(2, n+1):
    # 1을 빼는 연산
    dp[i] = dp[i-1] + 1
    # 만약, 2로 나눠지는 경우는 1로 뺀 값과 비교하여 작은 횟수를 저장.
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    # 만약, 3로 나눠지는 경우는 1로 뺀 값과 비교하여 작은 횟수를 저장.
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp)