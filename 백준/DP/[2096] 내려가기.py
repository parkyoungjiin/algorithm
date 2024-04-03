# import sys

# input = sys.stdin.readline
# n = int(input())
# graph = []
# for _ in range(n):
#     graph.append(list(map(int,input().split())))

# minDP = [[0] * n for _ in range(n)]
# maxDP = [[0] * n for _ in range(n)]

# # 0번지 : 0, 1
# # 1번지 : 0, 1, 2
# # 2번지 : 1, 2

# # minDP[1][0] = graph[1][0] + max(minDP[0][0], minDP[0][1])

# for i in range(n):
#     for j in range(3):
#         if i == 0:
#             minDP[i][j] += graph[i][j]
#             maxDP[i][j] += graph[i][j]
#         else:
#             if j == 0:
#                 minDP[i][j] = graph[i][j] + min(minDP[i-1][j], minDP[i-1][j+1])
#                 maxDP[i][j] = graph[i][j] + max(maxDP[i-1][j], maxDP[i-1][j+1])
#             elif j == 1:
#                 minDP[i][j] = graph[i][j] + min(minDP[i-1][j-1], minDP[i-1][j], minDP[i-1][j+1])
#                 maxDP[i][j] = graph[i][j] + max(maxDP[i-1][j-1], maxDP[i-1][j], maxDP[i-1][j+1])
#             else:
#                 minDP[i][j] = graph[i][j] + min(minDP[i-1][j-1], minDP[i-1][j])
#                 maxDP[i][j] = graph[i][j] + max(maxDP[i-1][j-1], maxDP[i-1][j])
# print(max(maxDP[-1]), min(minDP[-1]))
            
import sys

input = sys.stdin.readline

n = int(input())

max_dp = [0] * 3
min_dp = [0] * 3

max_tmp = [0] * 3
min_tmp = [0] * 3


for i in range(n):
    a, b, c = map(int, input().split())
    for j in range(3):
        if j == 0:
            max_tmp[j] = a + max(max_dp[j], max_dp[j + 1])
            min_tmp[j] = a + min(min_dp[j], min_dp[j + 1])
        elif j == 1:
            max_tmp[j] = b + max(max_dp[j - 1], max_dp[j], max_dp[j + 1])
            min_tmp[j] = b + min(min_dp[j - 1], min_dp[j], min_dp[j + 1])
        else:
            max_tmp[j] = c + max(max_dp[j], max_dp[j - 1])
            min_tmp[j] = c + min(min_dp[j], min_dp[j - 1])

    for j in range(3):
        max_dp[j] = max_tmp[j]
        min_dp[j] = min_tmp[j]

print(max(max_tmp), min(min_tmp)) 