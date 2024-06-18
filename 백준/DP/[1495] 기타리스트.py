import sys
input = sys.stdin.readline

n, s, max_vol = map(int, input().split())

volume = list(map(int, input().split()))

dp = [[0] * (max_vol+1) for _ in range(n+1)] # 곡 개수(n)만큼 최대 볼륨값 길이의 배열을 만든다.

dp[0][s] = 1 # 시작 볼륨을 첫 번째 곡의 볼륨에 1을 넣는다. 

for i in range(n):
    for j in range(max_vol+1): 
        if dp[i][j] == 1: 
            min_val = j - volume[i]
            max_val = j + volume[i]
            if min_val >= 0:
                dp[i+1][min_val] = 1

            if max_val <= max_vol:
                dp[i+1][max_val] = 1
result = -1
for i in range(max_vol, -1, -1): # (max_vol ~ -1) -1하면서 진행
    if dp[n][i] == 1: # 마지막 곡의 최대 볼륨 수 출력을 위해 [n][i]
        result = i
        break
print(result)
