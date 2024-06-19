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
    for i in range(n):
        if not visited[i] and prev != lst[i]:
            prev = lst[i]
            visited[i] = True
            dfs(i+1, ans+[lst[i]])
            visited[i] = False

dfs(0, [])