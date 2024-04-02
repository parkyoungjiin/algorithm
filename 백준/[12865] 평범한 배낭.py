import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (k+1) for _ in range(n+1)]
bag = [[0,0]]
for _ in range(n):
    k, v = map(int, input().split())
    bag.append([k,v])

for i in range(1, n+1):
    for j in range(1, k+1):
        # 현재최대무게가 해당물건무게보다 큰 경우
        if j >= bag[i][0]:
            dp[i][j] = max(bag[i][1] + dp[i-1][j-bag[i-1][0]], dp[i-1][j])
        # 작은 경우
        else:
            dp[i][j] = dp[i-1][j]

print(dp)