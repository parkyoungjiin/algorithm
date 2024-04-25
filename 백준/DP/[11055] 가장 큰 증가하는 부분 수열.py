import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int,input().split()))
dp = [0 for _ in range(n)]
dp[0] = arr[0]
print(dp)
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + arr[i])
        else:
            dp[i] = max(dp[i], arr[i])

print(dp)









# temp = []
#     if len(temp) == 0:
#         temp.append(arr[i])
#     elif temp[-1] < list[i]:
#         temp.append(arr[i])

#     if i == len(arr):
#         break
    
#     for j in range(i+1, len(arr)):
#         if temp[-1] < arr[j]:
#             temp.append(arr[j])
        
#     print(temp)