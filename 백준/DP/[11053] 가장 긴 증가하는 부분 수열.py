import sys
input = sys.stdin.readline

n = int(input())

num_lst = list(map(int,input().split()))

dp = [1] * n
dp[0] = num_lst[0]
for i in range(1, n):
    for j in range(i):
        if num_lst[i] > num_lst[j]:
            dp[i] = max(dp[i], num_lst[i] + dp[j])
        else:
            dp[i] = max(dp[i], num_lst[i])
            
print(max(dp))