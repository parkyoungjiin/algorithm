import sys
input = sys.stdin.readline
# dfs(인덱스, 결과값)
def dfs(index, result):
    global count
    if result == k:
        count += 1
        return
    if index == n:
        return
    
    dfs(index + 1, result + data[index])
    dfs(index + 1, result)


t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    data = list(map(int, input().split()))
    count = 0
    dfs(0,0)
    


