import sys
input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n+1)]
# print(dp)

for i in range(2, n+1):
    min_val = sys.maxsize
    # 제곱근인 경우 해당 i번지 DP에 1을 넣는다.
    if int(i ** 0.5) == (i**0.5):
        dp[i] = 1
    else:
        for j in range(1, i+1):
            if j * j > i:
                break
            if dp[i] > dp[i-(j*j)] + dp[j*j]:
                dp[i] = dp[i-(j*j)] + dp[j*j]

print(dp[n])


# for i in range(2, n+1):
#     min_val = sys.maxsize
#     # 제곱근인 경우 해당 i번지 DP에 1을 넣는다.
#     if int(i ** 0.5) == (i**0.5):
#         dp[i] = 1
#     else:
#         for j in range(1, (i//2)+1):
#             min_val = min(min_val, dp[i-j]+dp[j])

#         dp[i] = min_val