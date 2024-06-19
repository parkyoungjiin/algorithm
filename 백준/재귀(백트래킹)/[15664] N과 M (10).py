import sys
input = sys.stdin.readline

n, m = map(int, input().split())

lst = sorted(list(map(int, input().split())))
visited = [False] * n

def dfs(s, ans):
    if len(ans) == m:
        print(*ans)
        return
    
    prev = 0    
    for j in range(s, n):
        if prev != lst[j] and not visited[j]:
            prev = lst[j]
            visited[j] = True
            dfs(j+1, ans + [lst[j]])
            visited[j] = False

dfs(0, [])

# for i in range(n):
#     dfs(i, [])

