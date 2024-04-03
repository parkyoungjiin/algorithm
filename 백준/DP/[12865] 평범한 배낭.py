# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# bag = [(0,0)]
# dp = [[0] * (k+1) for _ in range(n+1)]

# for _ in range(n):
#     k, v = map(int, input().split())
#     bag.append((k,v))

# for i in range(1, n+1): #물건
#     for j in range(1, k+1): #1~k무게
#         # w = 무게, v = 물건가치
#         w = bag[i][0]
#         v = bag[i][1]

#         if j < w:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i-1][j], v + dp[i-1][j-w])

# print(dp)

import sys

n, k = map(int, sys.stdin.readline().split())  # 물품의 수, 버틸 수 있는 무게
arr = [(0, 0)]
chart = [[0] * (k + 1) for _ in range(n + 1)]
for _ in range(n):
    w, v = map(int, sys.stdin.readline().split())
    arr.append((w, v))

for i in range(1, n + 1):   # 물건 하나씩
    for j in range(1, k + 1):  # 1~k무게까지 표 작성
        w = arr[i][0]
        v = arr[i][1]
        if j < w:   # 해당 물건이 더 큰 경우, 이전 표값으로 넣기
            chart[i][j] = chart[i - 1][j]
        else:   # 해당 물건이 들어가는 사이즈인 경우
            chart[i][j] = max(chart[i - 1][j], v + chart[i - 1][j - w])    # 이전 값과 비교

print(chart)