import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))
visited = [False] * n
def dfs(s, tlst):
    if len(tlst) == m:
        print(*tlst)
        return
    
    prev = 0
    for i in range(s, n):
        if prev != lst[i] and not visited[i]:
            prev = lst[i]
            visited[i] = True
            dfs(i, tlst+[lst[i]])
            visited[i] = False

dfs(0, [])

