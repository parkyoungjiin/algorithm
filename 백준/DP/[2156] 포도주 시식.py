import sys
input = sys.stdin.readline

n = int(input())
grape = [int(input()) for _ in range(n)]
cnt = 1
dp = [0 for _ in range(n)]

dp[0] = grape[0]

# dp 갱신
for i in range(1,n):

    cnt += 1

    if cnt == 3:
        # 3번 연속인 경우는 직전의 dp 값으로 갱신 + cnt 초기화.

        cnt = 0
        dp[i] = max(grape[i], dp[i-1])
        continue

    dp[i] = max(grape[i], dp[i-1]+grape[i])
print(max(dp))
    
    




