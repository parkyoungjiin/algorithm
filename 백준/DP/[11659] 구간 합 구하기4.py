import sys
input = sys.stdin.readline

n, m = map(int,input().split())

numbers = list(map(int, input().split()))
dp = [0]
temp = 0
for i in range(n):
    temp += numbers[i]
    dp.append(temp)
    
for _ in range(m):
    i, j = map(int, input().split())
    # 점화식 = dp[j] - dp[i-1]
    print(dp[j] - dp[i-1])



