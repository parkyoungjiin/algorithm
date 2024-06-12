import sys
input = sys.stdin.readline

n, d = map(int, input().split())


shortcut = []
for _ in range(n):
    shortcut.append(list(map(int,input().split())))

shortcut.sort()

dp = [0 for _ in range(d+1)] # 거리 저장 DP (1차원)

k = 0 # k -> shortcut index

for i in range(d+1):
    dp[i] = min(dp[i-1]+1, dp[i])
    while k < n: # n = len(shortcut)
        if shortcut[k][0] == i: # start == i
            if shortcut[k][1] <= d:
                dp[shortcut[k][1]] = min(dp[i] + shortcut[k][2], dp[shortcut[k][1]])
            k+=1 # k++
        else:
            break
    









