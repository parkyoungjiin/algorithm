import sys

input = sys.stdin.readline

n, s = map(int, input().split())

num_lst = list(map(int, input().split()))
tlst = []
ans = 0
def dfs(start):
    global ans

    if sum(tlst) == s and len(tlst) > 0:
       ans += 1 


    for i in range(start, n):
        tlst.append(num_lst[i])
        dfs(i+1)
        tlst.pop()

dfs(0)
print(ans)    





# for i in range(n+1):
#     for j in range(i-1):
#         if sum(num_lst[j:i]) == s:
#             count += 1